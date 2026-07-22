from django.http import HttpResponse
from django.shortcuts import redirect, render
from . models import Task


# Create your views here.
def addtask(request):
    task1=request.POST['task']
    # this task has been written here ,becuase in the html page we have put name ='task' in the form action 
    Task.objects.create(task=task1)
    return redirect("home")