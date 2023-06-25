# Generated by Django 4.2.2 on 2023-06-25 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_generator', '0002_planet_atmosphere'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planet',
            name='atmosphere',
            field=models.BooleanField(default=True, help_text='Specify if planet would have some kind of atmosphere.'),
        ),
    ]
