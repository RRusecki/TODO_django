from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    objects = None
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
