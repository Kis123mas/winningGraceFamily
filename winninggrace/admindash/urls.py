from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.adminPage, name='adminpage'),

    path('programform/', views.programForm, name='programform'),
    path('updateprogram/<str:pk>/', views.updateProgram, name='updateprogram'),

    path('eventform/', views.eventForm, name='eventform'),
    path('updateevent/<str:pk>/', views.updateEvent, name='updateevent'),

    path('announcementform/', views.announcementForm, name='announcementform'),
    path('updateannouncement/<str:pk>/', views.updateAnnouncement, name='updateannouncement'),

    path('seedofwinform/', views.seedofwinForm, name='seedofwinform'),
    path('updateseedofwin/<str:pk>/', views.updateSeedofwin, name='updateseedofwin'),

    path('recommendedbibleform/', views.recommendedbibleForm, name='recommendedbibleform'),
    path('updaterecommendedbible/<str:pk>/', views.updateRecommendedBible, name='updaterecommendedbible'),
]