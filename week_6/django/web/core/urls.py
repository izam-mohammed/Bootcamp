from django.urls import path
from .views import login_user, signup_user, index, user_logout

urlpatterns = [
    path('', index, name='home'),
    path('login/', login_user, name='login'),
    path('signup/', signup_user, name='signup'),
    path('logout/', user_logout, name='logout'),
]
