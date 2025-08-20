from django.shortcuts import render
from rest_framework import viewsets
from .models import Students
from .serializer import StudentSerializer

# Create your views here.
class StudentView(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
