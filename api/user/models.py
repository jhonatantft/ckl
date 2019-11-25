from django.db import models
from interest.models import Interest

class User(models.Model):
    firstName = models.CharField(max_length=150)
    interests = models.ManyToManyField(Interest)

    def __str__(self):
        return self.firstName