from django.db import models
from .user_models import create_id, User


class Post(models.Model):
    id = models.CharField(default=create_id, primary_key=True, unique=True, max_length=10)
    body = models.TextField(max_length=200, blank=True)
    img = models.ImageField(blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
