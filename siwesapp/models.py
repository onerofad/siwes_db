from django.db import models

# Create your models here.
class Students(models.Model):
    matricno = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
