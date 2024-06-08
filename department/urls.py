from django.urls import re_path,path
from department import views


urlpatterns = [
    path("department/<int:id>", views.DepartmentAPIView.as_view()),
    path("department/", views.DepartmentAPIListView.as_view()),
]
