from bookshelf.models import Book
bookshelf = Book.objects.get(title="1984")
 print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")
