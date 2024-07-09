from django.urls import path
from .views import index, user_delete, user_edit, add_user

urlpatterns = [
    path('', index, name='index'),
    path('delete/<int:pk>', user_delete),
    path('edit/<int:pk>', user_edit),
    path('adduser/', add_user)
]