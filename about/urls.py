from . import views
from django.urls import path

# URL configuration for the 'about' app

urlpatterns = [
    # Maps the root URL of this app to the about_me view
    path('', views.about_me, name='about'),
]
