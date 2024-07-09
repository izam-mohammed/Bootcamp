from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView, MultipleObjectMixin

from posts.models import Category, Post, Tag

from .forms import UserDetailForm, UserForm

# Create your views here.


class ProfileDetailView(
    LoginRequiredMixin, MultipleObjectMixin, DetailView
):
    model = User
    template_name = "profile.html"
    paginate_by = 8  # Show 8 object per page.

    def get_object(self):
        request_user = get_object_or_404(
            User, username=self.request.user.username
        )
        return request_user

    # I was able to get the writers other posts using the code below. I did not have to show this code for this question. But just to show you that the pk above has to be username. Or Else the code below won't work(I guess)
    def get_context_data(self, **kwargs):
        object_list = Post.objects.filter(
            available=True, author=self.request.user
        )
        context = super(ProfileDetailView, self).get_context_data(
            object_list=object_list, **kwargs
        )
        # For Popular Posts
        context["popularposts"] = (
            Post.objects.filter(available=True)
            .annotate(viewyek=Count("views"))
            .order_by("-viewyek")[:3]
        )  # Get popular 3 posts
        context["categories"] = Category.objects.all()
        context["tags"] = Tag.objects.all()
        return context


class PasswordsChangeView(PasswordChangeView):
    template_name = "change-password.html"
    form_class = PasswordChangeForm
    success_url = reverse_lazy("user:viewProfile")

    def form_valid(self, form):
        messages.success(
            self.request,
            "Your password has been changed successfully.",
        )
        return super(PasswordsChangeView, self).form_valid(form)


class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    user_form = UserForm
    profile_form = UserDetailForm
    template_name = "profile_update.html"

    def post(self, request):
        post_data = request.POST or None
        file_data = request.FILES or None

        user_form = UserForm(post_data, instance=request.user)
        profile_form = UserDetailForm(
            post_data, file_data, instance=request.user.userdetail
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(
                request, "Your profile was successfully updated!"
            )
            return HttpResponseRedirect(
                reverse_lazy("user:updateProfile")
            )

        context = self.get_context_data(
            user_form=user_form, profile_form=profile_form
        )

        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request)


def registerView(request):
    if request.method == "POST":
        # user registration process
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if password == repassword:
            if (
                User.objects.filter(username=username).exists()
                or User.objects.filter(email=email).exists()
            ):
                messages.warning(
                    request, "Username or email is already taken."
                )
                return redirect("user:register")
            else:
                # registration
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password,
                )
                user.save()
                messages.success(
                    request,
                    "Registration created! You can login to your account.",
                )
                return redirect("user:login")
        else:
            messages.warning(request, "Passwords do not match.")
            return redirect("user:register")
    else:
        return render(request, "register.html")


def loginView(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(
            request, username=username, password=password
        )
        if user is not None:
            login(request, user)
            messages.success(
                request, "Login successful! Welcome, " + username
            )
            return redirect("pages:index")
        else:
            messages.error(
                request, "Check your information and try again!"
            )
            return redirect("user:login")
    else:
        return render(request, "login.html")


def logoutView(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect("user:login")


# Author Views


class AuthorIndexView(ListView):
    paginate_by = 8  # Show 8 object per page.
    model = User
    context_object_name = "author_list"
    template_name = "authors.html"
    post = Post.objects.filter(available=True).count()
    queryset = (
        User.objects.annotate(total_posts=Count("post"))
        .filter(total_posts__gt="0")
        .order_by("-total_posts")
    )  # Users with at least 1 share

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # For Popular Posts
        context["popularposts"] = (
            Post.objects.filter(available=True)
            .annotate(viewyek=Count("views"))
            .order_by("-viewyek")[:3]
        )  # Get popular 3 posts
        context["categories"] = Category.objects.all()
        context["tags"] = Tag.objects.all()
        return context


class AuthorDetailView(DetailView, MultipleObjectMixin):
    model = User
    template_name = "author_detail.html"
    context_object_name = "author"
    paginate_by = 8  # Show 8 object per page.

    def get_context_data(self, **kwargs):
        object_list = Post.objects.filter(
            available=True, author=self.get_object()
        )
        context = super(AuthorDetailView, self).get_context_data(
            object_list=object_list, **kwargs
        )
        # For Popular Posts
        context["popularposts"] = (
            Post.objects.filter(available=True)
            .annotate(viewyek=Count("views"))
            .order_by("-viewyek")[:3]
        )  # Get popular 3 posts
        context["categories"] = Category.objects.all()
        context["tags"] = Tag.objects.all()
        return context
