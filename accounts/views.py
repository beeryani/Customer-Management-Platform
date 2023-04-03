from django.forms import inlineformset_factory
from django.shortcuts import redirect, render

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .filters import OrderFilter
from .forms import CustomerForm, UpdateOrderForm, CreateUserForm
from .models import Customer, Order, Product


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

    order_filter = OrderFilter(request.GET, queryset=products_orders)
    products_orders = order_filter.qs

    data = {
        "customer_id": customer_id,
        "orders": no_orders,
        "products": products_orders,
        "order_filter": order_filter,
    }
    return render(request, "accounts/customer.html", data)


def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=("product", "status"))
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)

    if request.method == "POST":
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect("/")

    context = {"form": formset}
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


def loginUser(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("../")
        else:
            messages.info(request, "User or Password is incorrect")
            return render(request, "accounts/login.html", context)

    return render(request, "accounts/login.html", context)


def registerUser(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Account was created " + request.POST.get("username", " ")
            )
            return redirect("../login")

    context = {"form": form}
    return render(request, "accounts/register.html", context)


def logoutUser(request):
    logout(request)
    return redirect("../login/")
