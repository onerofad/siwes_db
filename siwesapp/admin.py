from django.contrib import admin
from .models import Students5, SiwesDetails, LocationDetails, PaymentDetails, Faculty, Department, Discipline

# Register your models here.
admin.site.register({Students5, SiwesDetails, LocationDetails, PaymentDetails, Faculty, Department, Discipline})

