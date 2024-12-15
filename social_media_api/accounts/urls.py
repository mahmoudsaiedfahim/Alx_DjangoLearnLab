
from django.urls import path, include
from .views import UserRegistrationView, CustomAuthToken
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
]