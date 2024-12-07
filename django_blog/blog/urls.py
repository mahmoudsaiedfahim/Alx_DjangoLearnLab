from django.urls import path # type: ignore
from django.contrib.auth import views as auth_views
from .views import register, HomeView, PostsView, ProfileView

urlpatterns = [

    path('', HomeView.as_view(template_name='blog/home.html'), name='home'),  # Define the home view
    path('login/',auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/',register, name='register'),
    path('profile/', ProfileView.as_view(template_name='blog/profile.html'), name='profile'),
    path('posts/', PostsView.as_view(template_name='blog/posts.html'), name='posts'),

]