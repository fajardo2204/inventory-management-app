from django.contrib import admin
from .models import Product
from django.contrib.auth.models import Group

admin.site.site_header = 'Inventory Management System Admin Panel'

# Register your models here.

admin.site.register(Product)

# admin.site.unregister(Group)