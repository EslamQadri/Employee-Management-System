from django.urls import re_path,path
from company import views


urlpatterns = [
    path("company/<int:id>", views.CompanyAPIView.as_view()),
    path("company", views.CompanyAPIListView.as_view()),
]
