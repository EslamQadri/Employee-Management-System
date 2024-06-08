from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from company.serializers import CompanySerializer
from company.models import Company
from employee.models import Employee
from company.permissions import IsCompanyOwnerOrSuperuser
from rest_framework.permissions import IsAuthenticated


class CompanyAPIView(APIView):
    permission_classes = [IsAuthenticated, IsCompanyOwnerOrSuperuser]

    def get(self, request, id, format=None):

        try:

            item = Company.objects.get(pk=id)
            serializer = CompanySerializer(item)
            return Response(serializer.data)

        except Company.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Company.objects.get(pk=id)
        except Company.DoesNotExist:
            return Response(status=404)
        serializer = CompanySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Company.objects.get(pk=id)
        except Company.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class CompanyAPIListView(APIView,IsCompanyOwnerOrSuperuser):

    def get(self, request, format=None):
        items = Company.objects.order_by("pk")
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = CompanySerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
