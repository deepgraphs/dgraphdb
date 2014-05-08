__author__ = 'mpetyx'

from django.db import models
from django.contrib.auth.models import User


class KnowledgeBase(models.Model):
    path = models.CharField(max_length=200)
    owner = models.ForeignKey(User)
    description = models.TextField()
    created = models.DateTimeField(auto_now=True)

