from django.utils import timezone
from django.db import models


class User(models.Model):
    username = models.CharField(unique=True, max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.username}"


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title} - {self.date_posted} - {self.author}"
