from django.db import models
from django.contrib.auth.models import AbstractUser
from company.models import Company
from department.models import Department
from employee.validators import mobile_number_regex
from django.utils import timezone


# Create your models here.
class UserAccounts(AbstractUser):
    ROLE_CHOICES = [
        ("admin", "Admin"),
        ("manager", "Manager"),
        ("employee", "Employee"),
        ("nothiredyet", "Not Hired Yet"),
    ]
    role = models.CharField(
        max_length=50, choices=ROLE_CHOICES, default="nothiredyet", blank=True
    )


class Employee(models.Model):
    TRANSITIONS_CHOICES = (
        ("ApplicationReceived", "Application Received"),
        ("InterviewScheduled", "Interview Scheduled"),
        ("Hired", "Hired"),
        ("NotAccepted", "Not Accepted"),
        ("left", "Left"),
    )
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    employee = models.OneToOneField(UserAccounts, on_delete=models.PROTECT)
    employee_status = models.CharField(
        "Employee Status", choices=TRANSITIONS_CHOICES, max_length=50
    )
    employee_name = models.CharField("Employee Name", max_length=500)
    email_address = models.EmailField("Email Address")
    mobile_number = models.CharField(
        "Mobile Number", validators=[mobile_number_regex], max_length=11, unique=True
    )
    address = models.TextField("Address")
    designation = models.CharField(
        "Designation ", help_text="Position or Title", max_length=144
    )
    hired_on = models.DateField("Hired on", blank=True, null=True)
    left_on = models.DateField("Left On", blank=True, null=True)

    @property
    def days_employed(self):
        if self.employee_status in ["Hired", "Left"] and self.hired_on:
            if self.employee_status == "Hired":
                return (timezone.now().date() - self.hired_on).days
            else:  # Assuming "Left" status means the employee has left the company
                if self.left_on:
                    return (self.left_on - self.hired_on).days
        return None

    @property
    def mark_as_left(self):
        if self.employee_status == "Left" and not self.left_on:
            self.left_on = timezone.now().date()
            self.save()

    def save(self, *args, **kwargs):

        if self.employee_status == "Hired" and not self.hired_on:
            self.hired_on = timezone.now().date()
        elif self.employee_status == "Left" and not self.left_on:
            self.left_on = timezone.now().date()
            self.save()

        super().save(*args, **kwargs)

    def get_department_queryset(self):
        return Department.objects.filter(company=self.company)

    def __str__(self) -> str:
        return f"{self.employee_name} with {self.mobile_number}"
