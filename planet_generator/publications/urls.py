"""URL patterns for 'publications' app."""

from django.urls import path

from . import views

app_name = "publications"
urlpatterns = [
    path('publish/<int:planet_id>', views.publish, name="publish"),
    path('publication/<int:planet_id>', views.publication, name="publication"),
    path('publications/', views.publications, name="publications"),
]
