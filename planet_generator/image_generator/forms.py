"""Forms for 'image_generator' app."""

from django.forms import ModelForm

from .models import Planet


class PlanetForm(ModelForm):
    """Form for creating new planet."""

    class Meta:
        model = Planet
        fields = [
            "name", "radius",
            "bulk_density", "albedo",
            "gravity", "resolution",
        ]
        labels = {'resolution': 'Image resolution (in pixels)'}
