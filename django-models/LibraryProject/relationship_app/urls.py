from django.urls import path
from . import views
from .views import list_books
from .views import LibraryDetailView
from .views import add_book
from .views import change_book
from .views import delete_book

from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk/>', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/templates/relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/templates/relationship_app/logout.html'), name= 'logout'),
    path('register/',views.register, name= 'register'),
    path('add_book/',add_book,name='add_book'),
    path('change_book/<int:pk>/',change_book,name='change_book'),
    path('delete_book/<int:pk>/',delete_book,name='delete_book'),
]