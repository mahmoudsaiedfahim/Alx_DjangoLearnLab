from django.shortcuts import render, redirect,get_object_or_404
from .forms import CustomUserCreationForm, CommentForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
class ProfileView(TemplateView):
    template_name = 'profile.html'

'''class PostsView(ListView):
    model = Post
    template_name = 'posts.html'''

class HomeView(TemplateView):
    template_name = 'home.html'


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_create'
    fields = ['title', 'content']
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author to the current user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'post_update'
    fields = ['title', 'content']
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Allow only the author to edit
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_delete'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Allow only the author to delete
    


"""
A view to add comments to a blog post.
"""
class CommentCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'post_detail.html'

    

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        form.instance.post = post
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.post.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, pk=self.kwargs['pk'])
        return context
    
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
    
   

"""
A view to update comments on a blog post.
"""
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment_update.html'

    # this gives a dynamic direction back to the post detail view after successful update 
    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.post.pk})
    
    # this ensures that the only the update comments
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
    

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'comment_delete.html'

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.post.pk})
    
    
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author