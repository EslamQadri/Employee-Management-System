from rest_framework.serializers import ModelSerializer
from company.models import Company
from rest_framework import serializers


class CompanySerializer(ModelSerializer):
    number_of_departments = serializers.ReadOnlyField()
    number_of_employees = serializers.ReadOnlyField()

    class Meta:
        model = Company
        fields = "__all__"

   
