from django.shortcuts import render
from rest_framework import viewsets
from .models import Students, SiwesDetails, LocationDetails, PaymentDetails, Faculty, Department, Discipline, StudentDetails
from .serializer import StudentSerializer, SiwesDetailsSerializer, LocationDetailsSerializer, PaymentDetailsSerializer, FacultySerializer, DepartmentSerializer, DisciplineSerializer, StudentDetailSerializer

# Create your views here.
class StudentView(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

class SiwesDetailsView(viewsets.ModelViewSet):
    queryset = SiwesDetails.objects.all()
    serializer_class = SiwesDetailsSerializer

class LocationDetailsView(viewsets.ModelViewSet):
    queryset = LocationDetails.objects.all()
    serializer_class = LocationDetailsSerializer

class PaymentDetailsView(viewsets.ModelViewSet):
    queryset = PaymentDetails.objects.all()
    serializer_class = PaymentDetailsSerializer

class FacultyView(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class DepartmentView(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DisciplineView(viewsets.ModelViewSet):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer

class StudentDetailsView(viewsets.ModelViewSet):
    queryset = StudentDetails.objects.all()
    serializer_class = StudentDetailSerializer