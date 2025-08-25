from django.db import models

# Create your models here.
class Students(models.Model):
    firstname = models.CharField(max_length=255, default="")
    middlename = models.CharField(max_length=255, default="")
    lastname = models.CharField(max_length=255, default="")
    matricno = models.CharField(max_length=255)
    programme = models.TextField(default='')
    faculty = models.TextField(default='')
    department = models.TextField(default='')
    discipline = models.TextField(default='')
    level = models.CharField(max_length=255, default='')
    gender = models.CharField(max_length=255, default='')
    phoneno = models.CharField(max_length=255, default='')
    email = models.TextField(default='')
    picture = models.TextField(default='')
    session = models.TextField(default='')
    password = models.CharField(default='')


    def __str__(self):
        return self.matricno
