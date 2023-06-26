from django.shortcuts import render, redirect

from image_generator.models import Planet
from .models import Publication
from .forms import PublicationForm


def publish(request, planet_id):
    """Make publication about planet."""
    planet = Planet.objects.get(id=planet_id)
    if request.method != 'POST':
        form = PublicationForm()
    else:
        form = PublicationForm(data=request.POST)
        if form.is_valid():
            new_pub = form.save(commit=False)
            new_pub.planet = planet
            new_pub.save()
            return redirect("img_generate:index")

    context = {"planet": planet, "form": form}
    return render(request, "publications/publish.html", context)


def publication(request, planet_id):
    """Show a single publication about planet."""
    publication = Publication.objects.get(planet_id=planet_id)
    return render(request, "publications/publication.html", {"publication": publication})
