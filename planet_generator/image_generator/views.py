"""Views for 'image_generator' app."""

from django.shortcuts import render, redirect

from .forms import PlanetForm


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
            form.save()
            return redirect("img_generate:index")

    context = {"form": form}
    return render(request, "image_generator/new_planet.html", context)
