from .models import Students, SiwesDetails, LocationDetails, PaymentDetails, Faculty, Department, Discipline
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Students

class SiwesDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = SiwesDetails

class LocationDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = LocationDetails

class PaymentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = PaymentDetails

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Faculty


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Department

class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Discipline