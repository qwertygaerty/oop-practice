from django.db.models.functions import Lower
from django.shortcuts import render

from .models import Book, Author, BookInstance, Genre


def index(request):
    """View function for home page of site."""

    # Generate counts of some main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    num_fantazy_genre = Genre.objects.annotate(
        uname=Lower('name')).filter(uname__icontains='фэнтези')

    num_hobbit_book = Book.objects.annotate(
        utitle=Lower('title')).filter(utitle__icontains='хоббит')

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_fantazy_genre': num_fantazy_genre,
        'num_hobbit_book': num_hobbit_book,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
