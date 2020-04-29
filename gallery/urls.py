from django.urls import path
from .views import home, contact, about, photos, photo, search, post_comments, delete_comment

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('gallery/', photos, name='gallery'),
    path('photo/<id>/', photo, name='photo'),
    path('search/', search, name='search'),
    path('post/<id>/<user>', post_comments, name='post'),
    path('delete/<id>/<photo_id>', delete_comment, name='delete'),
]
