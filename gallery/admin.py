from django.contrib import admin

# Register your models here.
from .models import Photo, Cart, Order, Contact

admin.site.register(Photo)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Contact)
