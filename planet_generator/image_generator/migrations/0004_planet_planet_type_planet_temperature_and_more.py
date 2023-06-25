# Generated by Django 4.2.2 on 2023-06-25 13:25

from django.db import migrations, models
import image_generator.models


class Migration(migrations.Migration):

    dependencies = [
        ('image_generator', '0003_alter_planet_atmosphere'),
    ]

    operations = [
        migrations.AddField(
            model_name='planet',
            name='planet_type',
            field=models.CharField(choices=[('terrestrial', 'Terrestrial'), ('gas giant', 'Gas Giant'), ('desert', 'Desert'), ('ice', 'Ice')], default='terrestrial', help_text='Planet type by composition.', max_length=200),
        ),
        migrations.AddField(
            model_name='planet',
            name='temperature',
            field=models.IntegerField(default=0, help_text='The average temperature on the planet (K).'),
        ),
        migrations.AlterField(
            model_name='planet',
            name='atmosphere',
            field=models.BooleanField(default=True, help_text='Specify whether planet would have some kind of atmosphere.'),
        ),
        migrations.AlterField(
            model_name='planet',
            name='bulk_density',
            field=models.DecimalField(decimal_places=4, help_text='Density computed using the total volume and mass of the planet (g*cm^(-3)).', max_digits=5, validators=[image_generator.models.validate_positive]),
        ),
        migrations.AlterField(
            model_name='planet',
            name='gravity',
            field=models.DecimalField(decimal_places=2, help_text="The gravitational acceleration on the planet's surface at the equator (m*s^(-2)).", max_digits=4, validators=[image_generator.models.validate_positive]),
        ),
        migrations.AlterField(
            model_name='planet',
            name='mass',
            field=models.DecimalField(decimal_places=5, help_text='Total mass of the planet (x10^24 kg).', max_digits=10, validators=[image_generator.models.validate_positive]),
        ),
        migrations.AlterField(
            model_name='planet',
            name='radius',
            field=models.DecimalField(db_column='mean_radius', decimal_places=4, help_text='Mean radius of the planet (km).', max_digits=11, validators=[image_generator.models.validate_positive]),
        ),
    ]