from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Photo
from django.contrib import messages



def home(request):
    return render(request, "gallery/home.html")


def exhibitions(request):
    return render(request, 'gallery/exhibitions.html', )


def about(request):
    return render(request, 'gallery/about.html.', )


def contact(request):
    return render(request, 'gallery/contact.html.', )


def photos(request):
    photos = Photo.objects.all()
    return render(request, 'gallery/gallery.html', {"photos": photos})

# Gives the information page of image.
def photo(request, id):
    photo = Photo.objects.get(id=id)
    return render(request, 'gallery/photo.html', {"photo": photo})

# Search bar functionality
def search(request):
    photos = Photo.objects.filter(title__icontains=request.GET['q'])
    return render(request, "gallery/gallery.html", {"photos": photos})