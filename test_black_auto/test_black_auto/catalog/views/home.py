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
    mailfunction = Malfunction.objects.all()

    context = {
        'mailfunction': mailfunction,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'mailfunction.html', context=context)

def glass(request):
    """View function for home page of site."""
    glass = Glass.objects.all()

    context = {
        'glass': glass,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'glass.html', context=context)
