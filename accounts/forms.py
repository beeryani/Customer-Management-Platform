from django.forms import ModelForm

from .models import *


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = "__all__"


class UpdateOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ["status"]


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
