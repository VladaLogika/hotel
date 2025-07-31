from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()
    likes_count = models.IntegerField()
    user_email = models.EmailField()
    def __str__(self):
        return self.title
    class Meta:
        ordering = ["created_at"]
# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=99)
    description = models.TextField(blank=True)
    capacity = models.IntegerField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ["created_at"]