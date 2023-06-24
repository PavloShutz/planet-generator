from django.urls import path

from . import views

app_name = "img_generate"
urlpatterns = [
    # Home page.
    path('', views.index, name="index"),
]
