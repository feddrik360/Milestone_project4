from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .form import Registration
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import auth

# Create your views here.



def register(request):
    if request.user.is_authenticated:
        return render(request, "gallery/home.html")
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = Registration()
    return render(request, 'users/registration.html', {'form' : form})

def login(request):
    if request.user.is_authenticated:
        return render(request,"gallery/home.html")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, 'These details are incorrect.')
            form = AuthenticationForm(request.POST)
            return render(request, "users/login.html", {'form': form})
    else:
        form = AuthenticationForm()
        return render(request,"users/login.html", {'form': form})

@login_required
def logout(request):
    auth.logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('/')