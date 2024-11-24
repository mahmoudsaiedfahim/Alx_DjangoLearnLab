#
from django.urls import path
from django.urls import include
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books-all',BookViewSet,basename='book-all')
'''urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
]'''

urlpatterns = [
    # Route for the BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),

    # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),  # This includes all routes registered with the router
]