# Generated by Django 4.2.2 on 2023-06-25 17:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('image_generator', '0004_planet_planet_type_planet_temperature_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='planet',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
