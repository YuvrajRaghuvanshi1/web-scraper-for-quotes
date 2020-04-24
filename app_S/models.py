from django.db import models

# Create your models here.
class Quotes(models.Model):
    quote=models.TextField()
    image = models.URLField(null=True, blank=True)