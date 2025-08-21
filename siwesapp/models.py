from django.db import models

# Create your models here.
class Students(models.Model):
    firstname = models.CharField(max_length=255, default="")
    middlename = models.CharField(max_length=255, default="")
    lastname = models.CharField(max_length=255, default="")
    matricno = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    middlename = models.CharField(max_length=255, default="")
    gender = models.CharField(max_length=255, default="")
    birthdate = models.DateField(default='21-08-2025')
    email = models.CharField(max_length=255, default="")
    phone = models.CharField(max_length=255, default="")
    residential_address = models.TextField(default="")
    residential_town = models.TextField(default="")
    lga = models.CharField(max_length=255, default="")
    country = models.CharField(max_length=255, default="")
    account_name = models.CharField(max_length=255, default="")
    bank_name = models.CharField(max_length=255, default="")
    account_no = models.CharField(max_length=255, default="")
    sort_code = models.CharField(max_length=255, default="")


    def __str__(self):
        return self.matricno
