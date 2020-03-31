from django.urls import path
from .views import home, GalleryView, contact, about, exhibitions

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('exhibitions/', exhibitions, name='exhibitions'),
    path('gallery/', GalleryView.as_view(), name='gallery'),

]
