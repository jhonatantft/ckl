from django.db import models
from newsCategory.models import NewsCategory

class News(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    source = models.CharField(max_length=150)
    url = models.CharField(max_length=150)
    postBy = models.CharField(max_length=150)
    publishDate = models.DateField(auto_now_add=True)
    createdAt = models.DateField(auto_now_add=True)
    readQuantity = models.IntegerField()
    categories = models.ForeignKey(NewsCategory, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title