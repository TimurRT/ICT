from django.db import models

# Create your models here.

class Painting(models.Model):

    title = models.CharField(max_length=123, verbose_name='Название')
    year = models.IntegerField(null=True)
    author = models.CharField(max_length=50)
    history = models.TextField(blank=True)

    def __str__(self):
        return self.title