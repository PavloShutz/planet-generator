"""URL patterns for 'users' app."""

from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path('register/', views.register, name="register"),
    path('portfolio/', views.portfolio, name="portfolio"),
]
