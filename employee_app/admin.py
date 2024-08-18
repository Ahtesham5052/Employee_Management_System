from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Role)

@admin.register(models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'bonus', 'salary', 'dept','role']
    list_per_page = 10


@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name','location']
    list_per_page = 10
    