from django.contrib import admin

from .models import Category, Comment, HitCount, Post, Tag

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name"]}
    list_display = ["name", "slug"]
    search_fields = ["name"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name"]}
    list_display = ["name", "slug"]
    search_fields = ["name"]


@admin.register(HitCount)
class HitCountAdmin(admin.ModelAdmin):
    list_display = ["ip"]
    search_fields = ["ip"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}
    list_display = [
        "title",
        "created",
        "category",
        "available",
        "getHitCount",
    ]
    list_display_links = ["title", "created"]
    list_filter = ["created", "category", "tags"]
    search_fields = ["title", "description"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["post", "author", "created", "available"]
    list_display_links = ["post", "author"]
    list_filter = ["post", "author", "created", "available"]
    search_fields = ["post", "author", "content"]
