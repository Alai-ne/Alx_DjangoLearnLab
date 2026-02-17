from django.shortcuts import render

# Create your view here
from django.views.generic import DetailView
from .models import Book, Library

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all().select_related('author')
    return render(request, 'list_books.html', {'books': books})

# Class-based view to display library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/list_books.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Ensure the books are available in the context
        context['books'] = self.object.books.all().select_related('author')
        return context
