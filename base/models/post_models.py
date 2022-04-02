from django.db import models
from .user_models import create_id, User
import os


def get_post_image_path(instance, filename):
    extends = filename.split('.')[-1]
    return os.path.join('post', f"{instance.id}.{extends}")


class Post(models.Model):
    id = models.CharField(default=create_id, primary_key=True, max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(default='', blank=True, max_length=150)
    img = models.ImageField(blank=True, null=True, upload_to=get_post_image_path)
    created_at = models.DateTimeField(auto_now_add=True)
    liked = models.ManyToManyField(User, related_name="favorited", blank=True)


class Comment(models.Model):
    id = models.CharField(default=create_id, primary_key=True, max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    liked = models.ManyToManyField(User, related_name="favorited_by", blank=True)
