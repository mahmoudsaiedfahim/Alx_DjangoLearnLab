from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.views.generic import TemplateView, ListView
from .models import Post

# Create your views here.
class PostsView(ListView):
    model = Post
    template_name = 'posts.html'

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
    return render(request, 'registration/register.html', {'form': form})


