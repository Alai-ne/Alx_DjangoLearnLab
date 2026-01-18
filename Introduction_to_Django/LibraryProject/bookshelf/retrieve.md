from bookshelf.models import Book
bookshelf = Book.objects.get(title="1984")
print(f"Title: {bookshelf.title}, Author: {bookshelf.author}, Year: {bookshelf.publication_year}")
