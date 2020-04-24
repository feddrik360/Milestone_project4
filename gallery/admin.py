from django.contrib import admin

# Register your models here.
from .models import Photo, Cart, Order, Contact,comment

admin.site.register(Photo)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Contact)
admin.site.register(comment)
