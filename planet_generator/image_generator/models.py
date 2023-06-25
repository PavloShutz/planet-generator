"""Models in 'image_generator' app."""

from decimal import Decimal

from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_albedo(albedo):
    """Validate if albedo's values range is from 0 to 1."""
    if Decimal(0) > albedo or Decimal(1) < albedo:
        raise ValidationError(
            _("%(albedo)s is not in range [0, 1]"),
            params={"albedo": albedo},
        )


def validate_positive(value):
    """Validate if given value is a positive number."""
    if value < 0:
        raise ValidationError(
            _("%(value)s must be a positive number"),
            params={"value": value},
        )


class Planet(models.Model):
    """Generated planet by user."""

    class ResolutionList(models.TextChoices):
        """List of available image resolutions in pixels."""
        LOW_RES = "256x256", "256x256"
        AVG_RES = "512x512", "512x512"
        HIGH_RES = "1024x1024", "1024x1024"

    name = models.CharField(
        max_length=150,
        help_text="Name of the planet.",
    )
    radius = models.DecimalField(
        max_digits=11,
        decimal_places=4,
        db_column="mean_radius",
        help_text="Mean radius of the planet.",
        validators=[validate_positive],
    )
    mass = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        help_text="Total mass of the planet.",
        validators=[validate_positive],
    )
    bulk_density = models.DecimalField(
        max_digits=5,
        decimal_places=4,
        help_text="Density computed using the total volume and mass of the planet.",
        validators=[validate_positive],
    )
    albedo_help_text = """
        Albedo is ratio of the light received by a body to the light reflected by that body.
        Albedo values range from 0 (pitch black) to 1 (perfect reflector).
    """
    albedo = models.DecimalField(
        max_digits=5,
        decimal_places=4,
        help_text=albedo_help_text,
        validators=[validate_positive, validate_albedo],
    )
    gravity = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        help_text="The gravitational acceleration on the planet's surface at the equator.",
        validators=[validate_positive],
    )
    atmosphere = models.BooleanField(
        default=True,
        help_text="Specify if planet would have some kind of atmosphere."
    )
    resolution = models.CharField(
        max_length=16,
        choices=ResolutionList.choices,
        default=ResolutionList.LOW_RES,
    )
    image = models.ImageField(
        upload_to='images/',
        help_text="Generated image of a planet."
    )

    def __str__(self):
        """Return name of the planet."""
        return self.name
