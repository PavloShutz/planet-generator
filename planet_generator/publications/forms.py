from django.forms import ModelForm

from publications.models import Publication


class PublicationForm(ModelForm):
    """Form for publication."""

    class Meta:
        model = Publication
        fields = ["pub_text"]
