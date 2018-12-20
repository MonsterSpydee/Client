from django.shortcuts import render, redirect
from django.conf import settings
from django.shortcuts import render_to_response

def home(request):
	return render(request,'startbootstrap-grayscale/index.html')

def register(request):
	return render(request, 'signup/signup.html')

def signin(request):
	return render(request, 'signin/signin.html')

def dashboard(request):
	return render(request, 'userprofile_template/dashboard.html')

def user(request):
	return render(request, 'userprofile_template/user.html')