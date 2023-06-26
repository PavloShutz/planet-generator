"""Module for generating picture of a planet."""

import urllib.request as url_request

import openai
from django.core.files import File

from planet_generator.settings import OPENAI_TOKEN

openai.api_key = OPENAI_TOKEN


def _generate_text_prompt(**kwargs) -> str:
    """
    Create text prompt for image generation.

    Keyword Args:
        mass: Total mass of the planet.
        radius: Mean radius of the planet.
        bulk_density: Density computed using the total volume and mass of the planet.
        albedo: Albedo is ratio of the light received by a body to the light reflected by that body.
                Albedo values range from 0 (pitch black) to 1 (perfect reflector).
        gravity: The gravitational acceleration on the planet's surface at the equator.
        atmosphere: Specify whether planet would have some kind of atmosphere.
        temperature: The average temperature on the planet.
        planet_type:

    Returns:
        Text prompt.
    """
    text_prompt = """Realistic planet with the following parameters:\n"""
    units_of_measurement = {
        'mass': 'x10^24 kg',
        'radius': 'km',
        'bulk_density': 'g*cm^(-3)',
        'gravity': 'm*s^(-2)',
        'temperature': 'K',
    }
    for param, value in kwargs.items():
        parameter = param.title().replace('_', ' ')
        if units_of_measurement.get(param):
            text_prompt += f"{parameter}: {value}{units_of_measurement[param]}\n"
        else:
            text_prompt += f"{parameter}: {value}\n"
    return text_prompt.rstrip()


def _generate_image_of_planet(prompt: str, size: str) -> str:
    """
    Generate image of planet based on text prompt and image's size.

    Args:
        prompt (str): Text prompt on which will be based the result.
        size (str): Size of a final image. Available values: 256x256, 512x512, or 1024x1024.

    Returns:
        Url of the generated picture.
    """
    response = openai.Image.create(
        prompt=prompt,
        n=1,  # specifying the number of images to be generated
        size=size,
    )
    return response["data"][0]["url"]


def save_planet_picture(planet, user) -> None:
    """
    Save path to image into a database.
    Args:
        planet: An instance of Planet model
        user: `request.user` instance
    Returns:
        None
    """
    prompt = _generate_text_prompt(
        mass=planet.mass,
        radius=planet.radius,
        bulk_density=planet.bulk_density,
        albedo=planet.albedo,
        gravity=planet.gravity,
        atmosphere=planet.atmosphere,
        temperature=planet.temperature,
        planet_type=planet.planet_type,
    )
    img_url = _generate_image_of_planet(prompt=prompt, size=planet.resolution)
    planet.owner = user
    filename = url_request.urlretrieve(img_url)[0]
    planet.image.save(
        f'{user.username}/{planet.name}.png',
        File(open(filename, 'rb')),
    )
