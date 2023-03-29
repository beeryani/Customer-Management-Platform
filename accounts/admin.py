from django.contrib import admin

from .models import Customer, Order, Product, Tag

admin.site.register([Customer, Product, Order, Tag])
