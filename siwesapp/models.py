from django.db import models

# Create your models here.
class Students(models.Model):
    firstname = models.CharField(max_length=255, default="")
    middlename = models.CharField(max_length=255, default="")
    lastname = models.CharField(max_length=255, default="")
    matricno = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.matricno
