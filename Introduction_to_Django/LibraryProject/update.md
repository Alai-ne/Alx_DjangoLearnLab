from bookshelf.models import Book
bookshelf = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
