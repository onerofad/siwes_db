from django.shortcuts import render
from rest_framework import viewsets
from .models import Students, SiwesDetails
from .serializer import StudentSerializer, SiwesDetailsSerializer

# Create your views here.
class StudentView(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

class SiwesDetailsView(viewsets.ModelViewSet):
    queryset = SiwesDetails.objects.all()
    serializer_class = SiwesDetailsSerializer