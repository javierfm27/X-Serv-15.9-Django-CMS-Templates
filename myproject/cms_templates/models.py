from django.db import models

# Create your models here.
class Pages (models.Model):
    nombreRec = models.CharField(max_length=32)
    contenido = models.TextField()
