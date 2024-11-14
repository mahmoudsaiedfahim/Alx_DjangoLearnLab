from django.shortcuts import render
from .models import Author, Book, Library, Librarian

# Create your views here.
def book_list(request):
    books = Book.objects.all()
    context = {'book_list':books}
    return render(request,'relationship_app/list_books.html',context)