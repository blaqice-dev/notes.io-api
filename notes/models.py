from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=155)
    text = models.TextField(max_length=5000, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=False, null=True, blank=True)
