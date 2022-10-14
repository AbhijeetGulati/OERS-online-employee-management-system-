from django.shortcuts import render
from django.http import HttpResponse
#importing all the reqd models
from .models import Employee,Dept,Role

# Create your views here.
#creating index function
def index(request):
    return render(request,'index.html')

def view_emp(request):
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    print(context)#if we dont print it we wont be able to see the values
    return render(request,'view_emp.html',context)

def add_emp(request):
    #here we will define the logic of this function
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        salary=int(request.POST['salary'])
        bonus=int(request.POST['bonus'])
        phone=request.POST['phone']
        dept=int(request.POST['dept'])
        role=int(request.POST['role'])
        
        new_emp=Employee(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,phone=phone,dept_id=dept,role_id=role)
        new_emp.save()
        return HttpResponse("Employee added successfully")

    elif request.method=='GET':
       return render(request,'add_emp.html')
    else:
        return HttpResponse("Exception Occured! Employee Not Added")

def remove_emp(request):
    return render(request,'remove_emp.html')

def filter_emp(request):
    return render(request,'filter_emp.html')
