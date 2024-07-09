import random

from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives, send_mail
from django.db.models import Count
from django.shortcuts import render
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views.generic.list import ListView

from posts.models import Category, Post, Tag

# Create your views here.


class LatestPostListView(ListView):
    model = Post
    template_name = "index.html"
    context_object_name = "latestposts"
    queryset = Post.objects.filter(available=True).order_by(
        "-created"
    )[:6]  # Get last 6 posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # For Random Posts
        post_count = Post.objects.filter(available=True).count()
        if post_count >= 3:
            items = list(Post.objects.filter(available=True))
            random_items = random.sample(items, 3)
            context["randomposts"] = random_items
        else:
            context["randomposts"] = Post.objects.filter(
                available=True
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


class AboutView(ListView):
    model = Post
    template_name = "about.html"

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


def ContactView(request):
    categories = Category.objects.all()
    tags = Tag.objects.all()
    popularposts = (
        Post.objects.filter(available=True)
        .annotate(viewyek=Count("views"))
        .order_by("-viewyek")[:3]
    )  # Get popular 3 posts

    context = {
        "popularposts": popularposts,
        "categories": categories,
        "tags": tags,
    }

    if request.method == "POST":
        subject = request.POST["subject"]
        email = request.POST["email"]
        message = request.POST["message"]
        try:
            html_content = render_to_string(
                "partials/mail_template.html",
                {"email": email, "message": message},
                request,
            )
            text_content = strip_tags(html_content)
            mail = EmailMultiAlternatives(
                subject,
                text_content,
                settings.EMAIL_HOST_USER,
                ["example@gmail.com"],
            )
            mail.attach_alternative(html_content, "text/html")
            mail.send()
            messages.success(request, "Your message has been sent.")
        except:
            messages.error(
                request,
                "We encountered an error sending your message, try again later..",
            )
        return render(request, "contact.html", context)

    return render(request, "contact.html", context)
