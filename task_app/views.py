from django.shortcuts import render,redirect
from django.http import HttpResponse
from task_app.forms import *
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

# Create your views here.

# <------Register page----->

def register(request):
    form = CustomUserForm()
    if request.method=='POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/my_login')
    return render(request,'register.html',{'form':form})

# <----Login page------>

def my_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request,data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username,password=password)

            if user is not None:
                auth.login(request,user)
                return redirect('/createtask')
    context = {'form':form}
    return render(request,'my_login.html',context=context)

# <-----Create tasks ------>

@login_required(login_url='my_login')
def createtask(request):
    form = CreateTaskForm()
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/viewtasks')
    context = {'form':form}
    return render(request,'create_task.html',context=context)

# <---- View tasks ------>

@login_required(login_url='my_login')
def viewtasks(request):       
    task = Task.objects.all()  
    context = {'tasks':task}
    return render(request,'view_tasks.html',context=context)

# <---- Update Task ------>

@login_required(login_url='my_login')
def updatetask(request,id):
    task = Task.objects.get(id=id)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/viewtasks')
    context = {'form':form}
    return render(request,'update_task.html',context=context)

# <---- Delete task ---->

@login_required(login_url='my_login')
def deletetask(request,id):
    task = Task.objects.get(id=id)    
    if request.method == 'POST':
        task.delete()
        return redirect('/viewtasks')
    context = {'object':task}
    return render(request,'delete_task.html',context=context)

# <--------logout----->

def user_logout(request):
    auth.logout(request)
    return redirect('/my_login')

