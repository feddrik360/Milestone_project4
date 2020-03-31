from django.shortcuts import render
from django.views.generic import ListView
from .models import Photo


# Create your views here.
def home(request):
    return render(request,"gallery/home.html")
def exhibitions(request):
    return render(request, 'gallery/exhibitions.html',)
def about(request):
    return render(request, 'gallery/about.html.',)
def contact(request):
    return render(request, 'gallery/contact.html.',)

class GalleryView(ListView):
    model = Photo
    template_name = "gallery/gallery.html"
