from typing import Any
from django.shortcuts import render
from .models import Author, Book, Library, Librarian
from django.views.generic import ListView, DetailView, TemplateView
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth import logout



# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {'book_list':books}
    return render(request,'relationship_app/list_books.html',context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['books'] = self.object.get.all()

'''# Creat an new user
user = User.objects.create_user('mahmoud', 'mahmoud@example.com', '1234')

# Retrieve a user based on a username
user = user.objects.get(username= 'mahmoud')'''

class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/templates/register.html'

class LoginView(LoginView):
    form_class = use

