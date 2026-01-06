from django.contrib import admin
from .models import Students3, SiwesDetails, LocationDetails, PaymentDetails, Faculty, Department, Discipline

# Register your models here.
admin.site.register({Students3, SiwesDetails, LocationDetails, PaymentDetails, Faculty, Department, Discipline})

