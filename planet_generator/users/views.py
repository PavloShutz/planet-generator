from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from image_generator.models import Planet


def register(request):
    """Register new user."""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect("img_generate:index")

    context = {"form": form}
    return render(request, "registration/register.html", context)


@login_required
def portfolio(request):
    """Show user's portfolio of his planet images."""
    planets = Planet.objects.filter(owner=request.user).all()
    context = {"planets": planets}
    return render(request, "users/portfolio.html", context)
