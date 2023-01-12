from django.db import models

class Post(models):
    title = models.CharField(max_length=32)
    user = models.CharField(max_length=32)
    content = models.TextField()
    region = models.CharField(max_length=16)
    price = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)