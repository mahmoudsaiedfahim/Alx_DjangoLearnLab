
from .models import Author, Book, Library, Librarian
books = Book.objects.all()
books_by_author = Book.objects.filter(author__name='')
library_name = ''
all_books_library = Library.objects.get(name = library_name)
library_instance = Library.objects.get(id = 1)
librarian = Librarian.objects.filter(library=library_instance)
