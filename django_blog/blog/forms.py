from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment
from taggit.forms import TagWidget

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class PostCreateForm(forms.ModelForm):
     title = forms.CharField(max_length=100)
     content = forms.Textarea()
     
     class Meta:
          model = Post
          fields = ['title', 'content', 'tags'] 
          widgets = {
            'tags': TagWidget(),
          }