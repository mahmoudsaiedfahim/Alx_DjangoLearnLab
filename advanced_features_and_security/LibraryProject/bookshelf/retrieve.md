Import:
from bookshelf.models import Book
Retrieve all:
Book.objects.all()
Retrieve by id:
Book.objects.get(id=3)
new_book.id

Retrieve by author:
Book.objects.get(author='George')
new_book.author

Retrieve by title:
Book.objects.get(title='1984')
new_book.title

Retrieve by publication_year:
Book.objects.get(publication_year=1949)
new_book.publication_year

