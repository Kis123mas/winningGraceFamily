from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.userdashPage, name='userpage'),
    path('profile', views.profilePage, name='profile'),
]