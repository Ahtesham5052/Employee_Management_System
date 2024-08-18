from django.db import models

# Create your models here.


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bonus = models.IntegerField(blank=True)
    salary = models.IntegerField()
    dept = models.ForeignKey('Department', on_delete=models.CASCADE, related_name="employee")
    role = models.ForeignKey('Role', on_delete=models.CASCADE, related_name="employee")

    def __str__(self) -> str:
        return self.first_name + self.last_name


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
