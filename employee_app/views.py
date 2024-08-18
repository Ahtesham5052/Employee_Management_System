from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse
from .models import Employee,Role,Department
# Create your views here.

def homepage(requests):
    return render(requests,'homepage.html')


def all_emp(requests):
    queryset = Employee.objects.all()
    return render(requests,'all_emp.html', {'employees':list(queryset)})


def add_emp(requests):
    if requests.method == 'POST':
        first_name = requests.POST['first_name']
        last_name = requests.POST['last_name']
        bonus = int(requests.POST['bonus'])
        salary = int(requests.POST['salary'])
        dept_name = requests.POST['dept']
        location = requests.POST['location']
        role_name = requests.POST['role']

        # Get or create the Department instance
        dept, created_dept = Department.objects.get_or_create(name=dept_name, location=location)

        # Get or create the Role instance
        role, created_role = Role.objects.get_or_create(name=role_name)

        # Create and save the new employee
        new_employee = Employee(first_name=first_name, last_name=last_name, bonus=bonus, salary=salary, dept=dept, role=role)
        new_employee.save()

        return HttpResponse('New Employee Added Successfully!')
    
    elif requests.method == 'GET':
        return render(requests, 'add_emp.html')
    
    else:
        return HttpResponse('Error Occurred')

def remove_emp(requests):
    if requests.method == 'POST':
        id = requests.POST['id']
        
        # Create and save the new employee
        employee = Employee(id=id)
        employee.delete()

        return HttpResponse('Employee Removed!')
    
    elif requests.method == 'GET':
        queryset = Employee.objects.all()
        return render(requests, 'remove_emp.html',{ "employees": list(queryset)})
    
    else:
        return HttpResponse('Error Occurred')


def filter_emp(requests):
    if requests.method == 'GET':
        return render(requests,'filter_emp.html')
    if requests.method == 'POST':
        if requests.POST['name']:
            name = requests.POST['name']
            queryset =  Employee.objects.filter(Q(first_name__istartswith=name) | Q(last_name__istartswith=name))
            return render(requests,"filter_emp.html",{'employees': list(queryset)})
        if requests.POST['department']:
            department = requests.POST['department']
            queryset =  Employee.objects.filter(dept__name__istartswith=department)
            return render(requests,"filter_emp.html",{'employees': list(queryset)})
        if requests.POST['role']:
            role = requests.POST['role']
            queryset =  Employee.objects.filter(role__name__istartswith=role)
            return render(requests,"filter_emp.html",{'employees': list(queryset)})