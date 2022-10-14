from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#creating index function
def index(request):
    return render(request,'index.html')

def view_emp(request):
    return render(request,'view_emp.html')

def add_emp(request):
    return render(request,'add_emp.html')

def remove_emp(request):
    return render(request,'remove_emp.html')

def filter_emp(request):
    return render(request,'filter_emp.html')
