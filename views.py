from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import GradeForm,CreateUserForm

def Home(request):
	return render(request,'home.html')

def registerPage(request):
	form = CreateUserForm
	
	if request.method == "POST":
		form = CreateUserForm(request.POST)
		if form.is_valid():	
			form.save()
	

	context = {'form':form}
	return render(request, 'addstudent.html',context)





