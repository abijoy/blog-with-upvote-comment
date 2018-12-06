from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	author = models.ForeignKey(User, on_delete=models.CASCADE)


class Upvote(models.Model):
	post = models.ForeignKey(Post, on_delete = models.CASCADE, default=1)
	user = models.ForeignKey(User, on_delete = models.CASCADE, default=1)

class Comment(models.Model):
	cmnt = models.TextField()
	user = models.ForeignKey(User, on_delete = models.CASCADE, default=1)
	post = models.ForeignKey(Post, on_delete = models.CASCADE, default=1)

