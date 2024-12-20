from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

user = get_user_model()

class Post(models.Model):
    author = models.ForeignKey(user, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self. title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(user, on_delete=models.PROTECT, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'



class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='liked')
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name='liked_by' ) 
    
    # Ensures a user can like a post only once
    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f"{self.user} liked {self.post}"
