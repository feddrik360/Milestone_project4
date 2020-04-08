from django.conf.urls import url
from .views import checkout
from django.urls import path

urlpatterns = [
    path('', checkout, name='checkout')
]
