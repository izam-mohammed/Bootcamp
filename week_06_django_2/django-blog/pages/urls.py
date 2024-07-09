from django.urls import path

from . import views

app_name = "pages"

urlpatterns = [
    path("", views.LatestPostListView.as_view(), name="index"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("contact/", views.ContactView, name="contact"),
]
