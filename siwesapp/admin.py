from django.contrib import admin
from .models import Students2, SiwesDetails, LocationDetails, PaymentDetails, Faculty, Department, Discipline

# Register your models here.
admin.site.register({Students2, SiwesDetails, LocationDetails, PaymentDetails, Faculty, Department, Discipline})

