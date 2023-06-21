from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('users/', views.userdashPage, name='userpage'),
    path('profile', views.profilePage, name='profile'),
    path('prayerrequest', views.prayerRequestPage, name='prayerrequest'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)