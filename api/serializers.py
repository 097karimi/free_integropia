from rest_framework import serializers
from .models import Student


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'last_name']
