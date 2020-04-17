from django.urls import path
from .views import register, login, logout, profile, update_profile,view_profile

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name ='profile'),
    path('update_profile/', update_profile ,name= 'update_profile'),
    path('view_profile/<id>', view_profile ,name= 'view_profile'),
]