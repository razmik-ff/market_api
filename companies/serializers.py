from rest_framework import serializers
from .models import Company

class CompanyGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = [
            'id',
            'name',
            'type',
            'address',
            'tel',
            'logo',
        ]
