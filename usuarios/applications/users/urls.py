from django.contrib import admin
from . import views
from django.urls import path
from .views import UserRegisterView

app_name= "users_app"

urlpatterns = [
    path(
        'register/', 
        views.UserRegisterView.as_view(),
        name='user-register',
    ),
    path(
        'login/', 
        views.LoginUser.as_view(),
        name='user-login',
    ),
    path(
        'logout/', 
        views.LogoutView.as_view(),
        name='user-logout',
    ),
    
]
