from django.db import models

# Create your models here.
class Students3(models.Model):
    title = models.CharField(max_length=255, default='')
    surname = models.CharField(max_length=255, default="")
    othernames = models.CharField(max_length=255, default="")
    matricno = models.CharField(max_length=255)
    programme = models.TextField(default='')
    faculty = models.TextField(default='')
    department = models.TextField(default='')
    gender = models.CharField(max_length=255, default='')
    state = models.CharField(max_length=255, default='')
    lga = models.CharField(max_length=255, default='')
    session = models.TextField(default='')
    password = models.CharField(max_length=255, default='password')
    payment_status = models.CharField(max_length=255, default='')
   

    def __str__(self):
        return self.matricno
    
class SiwesDetails(models.Model):
    endDate = models.DateField(default='2025-08-28')
    startDate = models.DateField(default='2025-08-28')
    deadline = models.DateField(default='2025-08-28')
    
    session = models.CharField(max_length=255, default='')
    department = models.CharField(max_length=255, default='')
    faculty = models.CharField(max_length=255, default='')
    matricno = models.CharField(max_length=255, default='')

    location = models.TextField(default='')
    location_id = models.IntegerField(default=0)
    amount = models.FloatField(default=0)
    siwes_address = models.TextField(default='')

    state_address = models.TextField(default='')
    city = models.CharField(max_length=255, default='')
    town = models.CharField(max_length=255, default='')
    street = models.TextField(default='')

    level = models.TextField(default='')
    email = models.TextField(default='')
    phone = models.TextField(default='')

    accountname = models.TextField(default='')
    accountno = models.TextField(default='')
    bankname = models.TextField(default='')

    whatsapp_phone = models.TextField(default='')
    bankcode = models.TextField(default='')
    sortcode = models.TextField(default='')



    def __str__(self):
        return self.matricno
    
class LocationDetails(models.Model):
    location_id = models.IntegerField(default=0)
    location = models.TextField()
    amount = models.FloatField()

    def __str__(self):
        return self.location
    
class PaymentDetails(models.Model):
    reference_id = models.CharField(max_length=255, default='')
    payment_date = models.DateField(auto_now_add=True)
    amount2 = models.FloatField(default=0)
    location = models.TextField(default='')
    matricno = models.CharField(max_length=255)
    fullname = models.TextField(default='')
    phoneno = models.CharField(max_length=255, default='')
    email = models.CharField(max_length=255, default='')
    status = models.CharField(max_length=255, default='')



    def __str__(self):
        return self.reference_id
    
class Faculty(models.Model):
    facultyName = models.CharField(max_length=255)
    facultyCode = models.CharField(max_length=255)

    def __str__(self):
        return self.facultyName
    

class Department(models.Model):
    departmentName = models.CharField(max_length=255)
    departmentCode = models.CharField(max_length=255)
    facultyCode = models.CharField(max_length=255)


    def __str__(self):
        return self.departmentName
    
class Discipline(models.Model):
    disciplineName = models.CharField(max_length=255)

    def __str__(self):
        return self.disciplineName


