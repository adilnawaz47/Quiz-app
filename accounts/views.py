from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
# Create your views here.
import sys
sys.setrecursionlimit(2000)
def login_attempt(request):
    if request.method =="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(email = email).first()
        if not user:
            message = {"error": "User does not exist"}
            context = message
            return render(request, 'auth/login.html', context)
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            message = {"error": "Invalid credentials"}
            context = message
            return render(request, 'auth/login.html', context)
    return render(request, 'auth/login.html')

def register_attempt(request):
    if request.method =="POST":
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(email = email).first()
        if user:
            message = {'error': "user already register"}
            context = message
            return render(request, 'auth/register.html', context)


        user = User(first_name = f_name, last_name = l_name, email = email, username = email)
        user.set_password(password)
        user.save()
        
    return render(request, 'auth/register.html')



def logout_view(request):
    logout(request)
    return redirect('/')

def thanks(request):
    return render(request, 'thanks.html')