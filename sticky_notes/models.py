from django.db import models
from django.urls import reverse


class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def __str__(self):
    return self.title


def get_absolute_url(self):
    return reverse('sticky_notes:note-detail', args=[self.pk])

