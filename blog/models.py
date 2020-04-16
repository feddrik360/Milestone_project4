from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from gallery.models import Photo


# Create your models here.

class comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

    def __str__(self):
        return self.user