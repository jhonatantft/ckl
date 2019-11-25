from django.db import models
from newsCategory.models import NewsCategory

class Interest(models.Model):
    name = models.CharField(max_length=150)
    categories = models.ForeignKey(NewsCategory, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name