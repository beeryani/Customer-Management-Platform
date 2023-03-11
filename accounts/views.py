from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import *
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

    data = {
        "customer_id": customer_id,
        "orders": no_orders,
        "products": products_orders,
    }
    return render(request, "accounts/customer.html", data)


def createOrder(request):
    form = OrderForm()

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {"form": form}
    return render(request, "accounts/order_form.html", context)


def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = UpdateOrderForm(instance=order)

    if request.method == "POST":
        form = UpdateOrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {"form": form}
    return render(request, "accounts/order_form.html", context)


def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect("/")

    context = {"order": order}
    return render(request, "accounts/delete_order.html", context)


def createCustomer(request):
    form = CustomerForm()

    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {"form": form}
    return render(request, "accounts/customer_form.html", context)


def updateCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)

    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {"form": form}
    return render(request, "accounts/customer_form.html", context)


def deleteCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method == "POST":
        customer.delete()
        return redirect("/")

    context = {"customer_id": customer}
    return render(request, "accounts/delete_customer.html", context)
