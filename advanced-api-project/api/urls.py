from django.urls import path
from .views import CustomBookCreateView, CustomBookListView, CustomBookDetailView, CustomBookDeleteView, CustomBookUpdateView

urlpatterns = [
    path('books/', CustomBookListView.as_view(), name='list'),
    path('books/<int:pk>', CustomBookDetailView.as_view(), name='detail'),
    path('books/create', CustomBookCreateView.as_view(), name='create'),
    path('books/update/<int:pk>', CustomBookUpdateView.as_view(), name='update'),
    path('books/delete/<int:pk>', CustomBookDeleteView.as_view(), name='delet'),

]
