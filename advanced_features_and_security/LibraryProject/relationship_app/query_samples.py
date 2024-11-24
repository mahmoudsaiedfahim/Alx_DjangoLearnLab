
from .models import Author, Book, Library, Librarian
all_books = Book.objects.all()
author_name = ''
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
library_name = ''
books = Library.objects.get(name=library_name)
all_books_library = books.all()
library_instance = Library.objects.get(id=1)
librarian = Librarian.objects.get(library=library_instance)
