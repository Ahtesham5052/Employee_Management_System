from django.shortcuts import render

# Create your views here.

def hello(requests):
    return render(requests,'hello.html')