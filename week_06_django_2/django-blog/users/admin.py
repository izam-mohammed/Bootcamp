from django.contrib import admin

from .models import UserDetail

# Register your models here.


@admin.register(UserDetail)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["user", "title", "description"]
    search_fields = ["username", "title", "description"]
