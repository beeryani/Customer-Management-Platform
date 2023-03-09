from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def home(request):
    customers = Customer.objects.all().order_by('-date_created')[:10]
    orders = Order.objects.all()
    data = {'customers': customers, 'orders': orders}
    return render(request, "accounts/dashboard.html", data)


def products(request):
    products = Product.objects.all()
    return render(request, "accounts/products.html", {'products': products})


def customer(request):
    return render(request, "accounts/customer.html")
