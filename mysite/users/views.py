from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
import logging

logger = logging.getLogger("users.views")

def sign_in(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('message')
        
        form = LoginForm()
        return render(request,'users/login.html', {'form': form})
    
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            # user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                messages.success(request,f'Hi {username.title()}, welcome back!')
                return redirect('message')
            logger.warning(f"Failed {username.title()} login attempt" )
       
        messages.error(request,f'Invalid username or password')
        return render(request,'users/login.html',{'form': form})
        
def sign_out(request):
    logout(request)
    messages.success(request,f'You have been logged out.')
    return redirect('login')  


def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})    
   
    if request.method == 'POST':
        form = RegisterForm(request.POST) 

        if form.is_valid():
            print(form.data)
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            if User.objects.filter(username=username).exists():
                form.add_error("username",'Username already taken')
                return render(request, 'users/register.html', {'form': form})
            
            new_user = User.objects.create_user(username=username, password=password) 
            messages.success(request, 'You have signed up successfully.')
            login(request, new_user)
            return redirect('message')
        else:
            return render(request, 'users/register.html', {'form': form})
