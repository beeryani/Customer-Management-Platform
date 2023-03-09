from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def home(request):
    customers = Customer.objects.all().order_by("-date_created")[:10]
    orders = Order.objects.all()

    orders_total = orders.count()
    orders_delivered = orders.filter(status="Delivered").count()
    orders_pending = orders.filter(status="Pending").count()

    data = {
        "customers": customers,
        "orders": orders,
        "orders_total": orders_total,
        "orders_delivered": orders_delivered,
        "orders_pending": orders_pending,
    }
    return render(request, "accounts/dashboard.html", data)


def products(request):
    products = Product.objects.all()
    return render(request, "accounts/products.html", {"products": products})


def customer(request, pk):
    customer_id = Customer.objects.get(id=pk)
    products_orders = Order.objects.filter(customer=customer_id)
    no_orders = products_orders.count()

    data = {"customer_id": customer_id, "orders": no_orders, "products": products_orders}
    return render(request, "accounts/customer.html", data)
