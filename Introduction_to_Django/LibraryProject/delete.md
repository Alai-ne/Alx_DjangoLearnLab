from bookshelf.models import Book
bookshelf = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
