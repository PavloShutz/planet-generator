"""Forms for 'image_generator' app."""

from django.forms import ModelForm

from .models import Planet


class PlanetForm(ModelForm):
    """Form for creating new planet."""

    class Meta:
        model = Planet
        fields = [
            "name", "radius",
            "temperature", "bulk_density",
            "albedo", "gravity",
            "atmosphere", "resolution",
        ]
        labels = {'resolution': 'Image resolution (in pixels)'}
