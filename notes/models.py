from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=155)
    text = models.TextField(max_length=5000)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
