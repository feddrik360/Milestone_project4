from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Photo(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    year = models.IntegerField()
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='art_2019')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("photo", kwargs={'slug': self.slug,})

class comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

    def __str__(self):
        return self.user

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.photo.title}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photos = models.ManyToManyField(Cart)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Contact(models.Model):
    forename = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()


    def __str__(self):
        return self.forename