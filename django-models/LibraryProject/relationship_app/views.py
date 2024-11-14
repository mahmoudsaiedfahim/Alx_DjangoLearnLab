from typing import Any
from django.shortcuts import render
from .models import Author, Book, Library, Librarian
from django.views.generic import ListView, DetailView, TemplateView
from .models import Library
from django.views.generic.detail import DetailView

# Create your views here.
def book_list(request):
    books = Book.objects.all()
    context = {'book_list':books}
    return render(request,'relationship_app/list_books.html',context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        