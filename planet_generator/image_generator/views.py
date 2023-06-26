"""Views for 'image_generator' app."""

from django.shortcuts import render, redirect

from .forms import PlanetForm
from . import image_generator as ig


def index(request):
    """Home page."""
    return render(request, 'image_generator/index.html')


def new_planet(request):
    """Generate new planet."""
    if request.method != 'POST':
        form = PlanetForm()
    else:
        form = PlanetForm(data=request.POST)
        if form.is_valid():
            new_planet = form.save(commit=False)
            ig.save_planet_picture(new_planet, request.user)
            new_planet.save()
            return redirect("img_generate:index")

    context = {"form": form}
    return render(request, "image_generator/new_planet.html", context)
