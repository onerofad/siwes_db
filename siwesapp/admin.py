from django.contrib import admin
from .models import Students, SiwesDetails, LocationDetails, PaymentDetails, Faculty, Department, Discipline

# Register your models here.
admin.site.register({Students, SiwesDetails, LocationDetails, PaymentDetails, Faculty, Department, Discipline})

