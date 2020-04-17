from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to = 'profile_pics')
    description = models.TextField()




    def __str__ (self):
        return self.user.username


def create_profile(sender, instance,created, **kwargs ):

    if created:
        Profile.objects.create(user = instance)
        print('Profile created!')
post_save.connect(create_profile, sender = User)

# def update_profile(sender,instance,created, **kwargs):

  #  if created == False:
   #     instance.Profile.save()
    #    print('Profile updated !')
 # post_save.connect(update_profile, sender=User)

# For singals decorators can be used as well.