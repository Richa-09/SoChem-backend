from django.db import models
from django.contrib.auth.models import User


class ForumPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    heading = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    author_name = models.TextField(max_length=50, default = "no_name")


class ForumComment(models.Model):
    parent_post = models.ForeignKey(ForumPost, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    date = models.DateTimeField(auto_now_add=True)
    author_name = models.TextField(max_length=50, default = "no_name")


class ForumReply(models.Model):
    parent_comment = models.ForeignKey(ForumComment, on_delete=models.CASCADE)
    reply = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    date = models.DateTimeField(auto_now_add=True)
