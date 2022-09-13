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

    num_fantazy_genre = Genre.objects.filter(name__icontains='fantasy').count()

    num_hobbit_book = Book.objects.filter(title__icontains='hobbit').count()

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


from django.views import generic


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'  # your own name for the list as a template variable

    def get_queryset(self):
        return Book.objects.filter(title__icontains='war')[:5]  # Get 5

    template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context
