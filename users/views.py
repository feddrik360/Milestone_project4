from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .form import Registration,UpdateProfile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import auth
from . models import Profile
from django.contrib.auth.models import User

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

def profile(request ):
    return render(request, "users/profile.html",)

def update_profile(request):
    if request.method == 'POST':
        Update_form =UpdateProfile(request.POST,request.FILES, instance = request.user.profile)
        if Update_form.is_valid():
            Update_form.save()
            messages.success(request, f'Your profile has been updated')
            return render(request, 'users/profile.html')
    else:
        form = UpdateProfile(instance = request.user.profile)
    return render(request, 'users/update_form.html', {"form" :form})

def view_profile(request, id):
    user = User.objects.get (id = id)
    profile = Profile.objects.get( user = user )
    return render(request, "users/view_profile.html",{"profile" : profile})


