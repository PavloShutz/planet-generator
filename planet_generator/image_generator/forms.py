"""Forms for 'image_generator' app."""

from django.forms import ModelForm
from django_bootstrap5.widgets import RadioSelectButtonGroup, RadioSelect

from .models import Planet


class PlanetForm(ModelForm):
    """Form for creating new planet."""

    class Meta:
        model = Planet
        fields = [
            "name", "radius", "mass",
            "temperature", "bulk_density",
            "albedo", "gravity",
            "atmosphere", "planet_type", "resolution",
        ]
        labels = {'resolution': 'Image resolution (in pixels)'}
        widgets = {
            'resolution': RadioSelectButtonGroup,
            'planet_type': RadioSelectButtonGroup
        }
