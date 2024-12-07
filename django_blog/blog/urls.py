from django.urls import path # type: ignore
from django.contrib.auth import views as auth_views
from .views import register, HomeView, ProfileView
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [

    path('', HomeView.as_view(template_name='blog/home.html'), name='home'),  # Define the home view
    path('login/',auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/',register, name='register'),
    path('profile/', ProfileView.as_view(template_name='blog/profile.html'), name='profile'),
    #path('posts/', PostsView.as_view(template_name='blog/posts.html'), name='posts'),

    path('posts/', PostListView.as_view(template_name='blog/post_list.html'), name='post-list'),  # List all posts
    path('post/<int:pk>/', PostDetailView.as_view(template_name='blog/post_detail.html'), name='post-detail'),  # Detail view for a single post
    path('post/new/', PostCreateView.as_view(template_name='blog/post_create.html'), name='post-create'),  # Create a new post
    path('post/<int:pk>/edit/', PostUpdateView.as_view(template_name='blog/post_update.html'), name='post-update'),  # Edit an existing post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(template_name='blog/post_delete.html'), name='post-delete'),  # Delete a post
]