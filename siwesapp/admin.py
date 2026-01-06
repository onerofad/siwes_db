from django.contrib import admin
from .models import Students4, SiwesDetails, LocationDetails, PaymentDetails, Faculty, Department, Discipline

# Register your models here.
admin.site.register({Students4, SiwesDetails, LocationDetails, PaymentDetails, Faculty, Department, Discipline})

