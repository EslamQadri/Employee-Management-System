from django.contrib import admin
from employee.models import Employee, UserAccounts





# Register your models here.
admin.site.register((Employee, UserAccounts))
