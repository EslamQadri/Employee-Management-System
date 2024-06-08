from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from department.serializers import DepartmentSerializer
from department.models import Department


class DepartmentAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Department.objects.get(pk=id)
            serializer = DepartmentSerializer(item)
            return Response(serializer.data)
        except Department.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Department.objects.get(pk=id)
        except Department.DoesNotExist:
            return Response(status=404)
        serializer = DepartmentSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Department.objects.get(pk=id)
        except Department.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class DepartmentAPIListView(APIView):

    def get(self, request, format=None):
        items = Department.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = DepartmentSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
