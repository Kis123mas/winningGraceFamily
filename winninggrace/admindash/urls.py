from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', views.adminPage, name='adminpage'),

    path('programform/', views.programForm, name='programform'),
    path('updateprogram/<str:pk>/', views.updateProgram, name='updateprogram'),
    path('deleteprogram/<str:pk>/', views.deleteProgram, name='deleteprogram'),

    path('eventform/', views.eventForm, name='eventform'),
    path('updateevent/<str:pk>/', views.updateEvent, name='updateevent'),
    path('deleteevent/<str:pk>/', views.deleteEvent, name='deleteevent'),

    path('announcementform/', views.announcementForm, name='announcementform'),
    path('updateannouncement/<str:pk>/', views.updateAnnouncement, name='updateannouncement'),
    path('deleteannouncement/<str:pk>/', views.deleteAnnouncement, name='deleteannouncement'),

    path('seedofwinform/', views.seedofwinForm, name='seedofwinform'),
    path('updateseedofwin/<str:pk>/', views.updateSeedofwin, name='updateseedofwin'),
    path('deleteseedofwin/<str:pk>/', views.deleteSeedofwin, name='deleteseedofwin'),

    path('recommendedbibleform/', views.recommendedbibleForm, name='recommendedbibleform'),
    path('updaterecommendedbible/<str:pk>/', views.updateRecommendedBible, name='updaterecommendedbible'),
    path('deleterecommendedbible/<str:pk>/', views.deleteRecommendedBible, name='deleterecommendedbible'),
]