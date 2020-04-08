from django.db import models
from gallery.models import Photo



class Information(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=200, blank=False)
    country = models.CharField(max_length=25, blank=False)
    postcode = models.CharField(max_length=15, blank=False)
    address = models.CharField(max_length=100, blank=False)
    county = models.CharField(max_length=30, blank=False)
    date = models.DateField()

    def __str__(self):
        return self.first_name

class Order(models.Model):
    order = models.ForeignKey(Information, null=False, on_delete=models.CASCADE)
    product = models.ForeignKey(Photo, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return self.product.name
