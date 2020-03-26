from django.db import models

# Create your models here.

class Photo(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    date = models.IntegerField()
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='art_2019')

    def __str__(self):
        return self.title

