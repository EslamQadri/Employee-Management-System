from rest_framework.serializers import ModelSerializer
from department.models import Department
from rest_framework import serializers


class DepartmentSerializer(ModelSerializer):
    number_of_employees = serializers.ReadOnlyField()

    class Meta:
        model = Department
        fields = "__all__"
        depth = 1
