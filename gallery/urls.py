from django.urls import path
from .views import home,  contact, about, exhibitions, photos, photo, search

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('exhibitions/', exhibitions, name='exhibitions'),
    path('gallery/', photos, name='gallery'),
    path('photo/<id>/', photo, name='photo'),
    path('search/',search, name = 'search')

]
