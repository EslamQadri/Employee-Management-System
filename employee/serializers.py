from rest_framework.serializers import ModelSerializer
from employee.models import UserAccounts, Employee
from rest_framework import serializers


class UserAccountsSerializer(ModelSerializer):

    class Meta:
        model = UserAccounts
        fields = "__all__"


class EmployeeSerializer(ModelSerializer):
    days_employed = serializers.ReadOnlyField()

    class Meta:
        model = Employee
        fields = "__all__"
        depth = 1



class UserSerializer(ModelSerializer):
    class Meta:
        model = UserAccounts
        fields = ("username", "email", "password", "first_name", "last_name",)
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = UserAccounts.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )
        return user
class UserLoginSerializer(ModelSerializer):
    class Meta:
        model = UserAccounts
        fields = ("username", "password")
        extra_kwargs = {"password": {"write_only": True}}