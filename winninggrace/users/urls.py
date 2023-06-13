from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', views.registerPage, name='registerpage'),
    path('login/', views.loginPage, name='loginpage'),
    path('logout/', views.logoutMember, name='logout'),
]