from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = "user"

urlpatterns = [
    path("register/", views.registerView, name="register"),
    path("login/", views.loginView, name="login"),
    path("logout/", views.logoutView, name="logout"),
    path(
        "profile/detail",
        views.ProfileDetailView.as_view(),
        name="viewProfile",
    ),
    path(
        "profile/update",
        views.ProfileUpdateView.as_view(),
        name="updateProfile",
    ),
    path(
        "change-password",
        views.PasswordsChangeView.as_view(
            template_name="change-password.html"
        ),
        name="changePassword",
    ),
    path("all/", views.AuthorIndexView.as_view(), name="authors"),
    path(
        "detail/<int:pk>",
        views.AuthorDetailView.as_view(),
        name="authorDetail",
    ),
]
