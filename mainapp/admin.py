# Register your models here.

from django.contrib import admin

from .models import Contact, Product, ProductCategory

admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Contact)
