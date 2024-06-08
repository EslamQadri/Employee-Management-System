from django.db import models


# Create your models here.
class Company(models.Model):
    company_name = models.CharField("Company Name", max_length=500)

    @property
    def number_of_departments(self):
        from department.models import Department

        """
        using lazy import within the property method, 
        you avoid the circular import since Department is only imported when the method is called,
         not during module import.
        """
        return Department.objects.filter(company=self).count()

    @property
    def number_of_employees(self):
        from employee.models import Employee

        return Employee.objects.filter(company=self).count()

    def __str__(self) -> str:
        return f"{self.company_name}"
