from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=64)
    date = models.DateTimeField()
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,)
    body = models.TextField()
    def __str__(self):
        return "%s (%s)" % (self.title,self.author)
    def snippet(self):
        return self.body[:50] + '...'
