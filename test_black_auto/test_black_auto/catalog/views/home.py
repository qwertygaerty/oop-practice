from django.shortcuts import render

from ..models import CarModel, CarMalfunction, Malfunction, Brand, Glass, GlassType


def index(request):
    """View function for home page of site."""
    brands = Brand.objects.all()

    context = {
        'brands': brands,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


def malfunction(request):
    """View function for home page of site."""
    mailfunctions = Malfunction.objects.all()

    context = {
        'mailfunctions': mailfunctions,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'mailfunctions.html', context=context)
