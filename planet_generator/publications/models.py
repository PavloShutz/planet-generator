from django.db import models

from image_generator.models import Planet


class Publication(models.Model):
    """Publication of a planet."""

    planet = models.OneToOneField(
        Planet,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    pub_text = models.TextField(
        "publication text",
        max_length=5000,
        blank=True,
    )
