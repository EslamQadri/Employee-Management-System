from django.urls import re_path, path
from employee import views


urlpatterns = [
    path("useraccounts/<int:id>", views.UserAccountsAPIView.as_view()),
    path("useraccounts/", views.UserAccountsAPIListView.as_view()),
   path("employee/<int:id>", views.EmployeeAPIView.as_view()),
    path("employee/", views.EmployeeAPIListView.as_view()),
    path("signup", views.UserSignup.as_view()),
    path("login", views.UserLogin.as_view()),
]
