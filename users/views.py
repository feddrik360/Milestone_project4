from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .form import Registration

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = Registration()
    return render(request, 'users/registration.html', {'form' : form})

