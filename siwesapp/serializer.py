from .models import Students, SiwesDetails
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Students

class SiwesDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = SiwesDetails