from django.db import models
from company.models import Company


# Create your models here.
class Department(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    department_name = models.CharField("Department Name", max_length=500)

    @property
    def number_of_employees(self):
        from employee.models import Employee

        return Employee.objects.filter(department=self).count()

    def __str__(self) -> str:
        return f"{self.department_name} at {self.company.company_name} "
