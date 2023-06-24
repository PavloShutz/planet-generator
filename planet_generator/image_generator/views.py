from django.shortcuts import render

from .forms import PlanetForm


def index(request):
    """Home page."""
    return render(request, 'image_generator/index.html')


def new_planet(request):
    """Generate new planet."""
    pass
