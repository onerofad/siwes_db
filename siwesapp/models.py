from django.db import models

# Create your models here.
class Students(models.Model):
    title = models.CharField(max_length=255, default='')
    surname = models.CharField(max_length=255, default="")
    othernames = models.CharField(max_length=255, default="")
    matricno = models.CharField(max_length=255)
    birthdate = models.TextField(default="")
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
    surname = models.CharField(max_length=255)
    othernames = models.CharField(max_length=255)
    phoneno = models.CharField(max_length=255, default='')
    email = models.CharField(max_length=255, default='')

    

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

class StudentDetails(models.Model):
    MatricNo = models.CharField(max_length=255)
    Surname = models.CharField(max_length=255)
    OtherNames = models.CharField(max_length=255)
    Gender = models.CharField(max_length=255)
    Faculty= models.CharField(max_length=255)
    Department = models.CharField(max_length=255)
    Discipline = models.CharField(max_length=255)
    Programme = models.CharField(max_length=255)
    Level = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    Phone = models.CharField(max_length=255)
    PictureLink = models.TextField()

    def __str__(self):
        return self.MatricNo

