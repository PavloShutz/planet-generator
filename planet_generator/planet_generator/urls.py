"""
URL configuration for planet_generator project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('image_generator.urls')),
]
