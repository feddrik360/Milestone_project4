from django.shortcuts import render
from django.views.generic import ListView
from .models import Photo


# Create your views here.
def home(request):
    return render(request,"gallery/home.html")

class GalleryView(ListView):
    model = Photo
    template_name = "gallery/gallery.html"
