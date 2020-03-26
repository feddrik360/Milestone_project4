from django.urls import path
from .views import home, GalleryView

urlpatterns = [
    path('', home, name= 'home'),
    path('gallery/',GalleryView.as_view() , name= 'gallery')
]
