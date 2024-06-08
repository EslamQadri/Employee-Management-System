from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from employee.serializers import (
    UserAccountsSerializer,
    EmployeeSerializer,
    UserSerializer,
    UserLoginSerializer,
)
from employee.models import UserAccounts, Employee
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from company.permissions import IsCompanyOwnerOrSuperuser


class UserAccountsAPIView(APIView,IsCompanyOwnerOrSuperuser):

    def get(self, request, id, format=None):
        try:
            item = UserAccounts.objects.get(pk=id)
            serializer = UserAccountsSerializer(item)
            return Response(serializer.data)
        except UserAccounts.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = UserAccounts.objects.get(pk=id)
        except UserAccounts.DoesNotExist:
            return Response(status=404)
        serializer = UserAccountsSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = UserAccounts.objects.get(pk=id)
        except UserAccounts.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class UserAccountsAPIListView(APIView,IsCompanyOwnerOrSuperuser):

    def get(self, request, format=None):
        items = UserAccounts.objects.order_by("pk")
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = UserAccountsSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = UserAccountsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class EmployeeAPIView(APIView,IsCompanyOwnerOrSuperuser):

    def get(self, request, id, format=None):
        try:
            item = Employee.objects.get(pk=id)
            serializer = EmployeeSerializer(item)
            return Response(serializer.data)
        except Employee.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Employee.objects.get(pk=id)
        except Employee.DoesNotExist:
            return Response(status=404)
        serializer = EmployeeSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Employee.objects.get(pk=id)
        except Employee.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class EmployeeAPIListView(APIView,IsCompanyOwnerOrSuperuser):

    def get(self, request, format=None):
        items = Employee.objects.order_by("pk")
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = EmployeeSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def UserInfo(request):
    try:
        emp = Employee.objects.get(email_address=request.user.email)
        return Response({"employee_status": emp.employee_status}, status=200)
    except Employee.DoesNotExist:
        return Response({"detail": "Your email is not in the system"}, status=404)


from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


class UserLogin(generics.CreateAPIView):
    queryset = UserAccounts.objects.all()
    serializer_class = UserLoginSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        data = request.data
        username = data.get("username", None)
        password = data.get("password", None)
        print(username, password)
        if username is None or password is None:
            return Response(
                {"error": "Please provide both username and password."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = UserAccounts.objects.filter(username=username).first()
        print(user)
        if user is None or not user.check_password(password):
            print("ss")
            return Response(
                {"error": "Invalid username or password."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        refresh = RefreshToken.for_user(user)
        return Response(
            {"access_token": str(refresh.access_token), "refresh_token": str(refresh)},
            status=status.HTTP_200_OK,
        )


class UserSignup(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)
