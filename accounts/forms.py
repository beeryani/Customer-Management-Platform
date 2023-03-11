from django.forms import ModelForm

from .models import *


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = "__all__"


class UpdareOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ["status"]
