from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.template.defaultfilters import slugify
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    DeleteView,
    UpdateView,
)

from .models import Category, Comment, HitCount, Post, Tag

# Create your views here.


class CommentView(LoginRequiredMixin, CreateView):
    template_name = "comment_create.html"
    model = Comment
    fields = ["content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs["pk"]
        messages.success(self.request, "Comment successfully added.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            "posts:postDetail",
            args=(
                self.object.post.category.slug,
                self.object.post.pk,
                self.object.post.slug,
            ),
        )


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "post_create.html"
    model = Post
    fields = ["category", "tags", "title", "image", "content"]

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.slug = slugify(post.title)
        counter = 1
        temp_slug = post.slug

        while Post.objects.filter(
            slug=post.slug
        ).exists():  # If there is the same information in the database, it is created by adding 1 to the end.
            post.slug = "{}-{}".format(temp_slug, counter)
            counter += 1

        form.save()
        messages.success(
            self.request, "Your post has been successfully created."
        )
        return super(PostCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse(
            "posts:postDetail",
            args=(
                self.object.category.slug,
                self.object.id,
                self.object.slug,
            ),
        )


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = "post_update.html"
    template_name_suffix = "_update_form"
    fields = ["category", "tags", "title", "image", "content"]

    @method_decorator(login_required)  # If logged in this works
    def dispatch(self, request, *args, **kwargs):
        post = self.get_object()
        if post.author != self.request.user:
            raise Http404("You are not allowed to edit this Post")
        return super(PostUpdateView, self).dispatch(
            request, *args, **kwargs
        )

    def form_valid(self, form):
        post = form.save(commit=False)
        post.slug = slugify(post.title)
        counter = 1
        temp_slug = post.slug

        dbpost = Post.objects.get(id=post.id)
        if (
            dbpost.title != post.title
        ):  # Do these if the title of the post has changed
            while Post.objects.filter(
                slug=post.slug
            ).exists():  # If there is the same information in the database, it is created by adding 1 to the end.
                post.slug = "{}-{}".format(temp_slug, counter)
                counter += 1

        form.save()
        messages.success(
            self.request, "Your post has been successfully updated."
        )
        return super(PostUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse(
            "posts:postDetail",
            args=(
                self.object.category.slug,
                self.object.id,
                self.object.slug,
            ),
        )


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("user:viewProfile")

    def get_object(self, queryset=None):
        post = super(PostDeleteView, self).get_object()
        if not post.author == self.request.user:
            raise Http404("You are not allowed to delete this Post")
        return post

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Post successfully deleted.")
        return super(PostDeleteView, self).delete(
            request, *args, **kwargs
        )


def PostList(request, category_slug=None, tag_slug=None):
    category_page = None
    tag_page = None
    categories = Category.objects.all()
    tags = Tag.objects.all()
    popularposts = (
        Post.objects.filter(available=True)
        .annotate(viewyek=Count("views"))
        .order_by("-viewyek")[:3]
    )  # Get popular 3 posts
    context = {}

    if category_slug is not None:
        category_page = get_object_or_404(
            Category, slug=category_slug
        )
        posts = Post.objects.filter(
            available=True, category=category_page
        ).order_by("-created")
        context.update({"title": "Posts By Category"})
    elif tag_slug is not None:
        tag_page = get_object_or_404(Tag, slug=tag_slug)
        posts = Post.objects.filter(
            available=True, tags=tag_page
        ).order_by("-created")
        context.update({"title": "Posts By Tag"})
    else:
        posts = (
            Post.objects.all()
            .filter(available=True)
            .order_by("-created")
        )
        context.update({"title": "All Posts"})

    paginator = Paginator(posts, 8)  # Show 8 object per page.
    page_number = request.GET.get("page")
    post_list = paginator.get_page(page_number)

    context.update({
        "post_list": post_list,
        "popularposts": popularposts,
        "categories": categories,
        "tags": tags,
    })
    return render(request, "posts.html", context)


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # For Popular Posts
        context["popularposts"] = (
            Post.objects.filter(available=True)
            .annotate(viewyek=Count("views"))
            .order_by("-viewyek")[:3]
        )  # Get popular 3 posts

        context["relatedposts"] = (
            Post.objects.filter(
                available=True,
                category__name=self.object.category.name,
            )
            .annotate(viewyek=Count("views"))
            .order_by("-viewyek")[:3]
        )  # Get related 3 popular posts

        context["categories"] = Category.objects.all()
        context["tags"] = Tag.objects.all()
        context["comments"] = Comment.objects.filter(
            available=True, post_id=self.object.id
        ).order_by("-created")[:10]  # Get last 10 comments
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        ip = get_client_ip(self.request)
        if HitCount.objects.filter(ip=ip).exists():
            pass
        else:
            HitCount.objects.create(ip=ip)
        post = Post.objects.get(pk=self.object.pk)
        post.views.add(HitCount.objects.get(ip=ip))
        return self.render_to_response(context)


def search(request):
    posts = Post.objects.filter(
        Q(title__icontains=request.GET["query"])
        | Q(content__icontains=request.GET["query"])
    )
    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = {
        "post_list": posts,
        "categories": categories,
        "tags": tags,
        "title": "Search Results",
    }
    return render(request, "posts.html", context)
