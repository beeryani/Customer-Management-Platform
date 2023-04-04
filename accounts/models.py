from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=30, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    profile_picture = models.ImageField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.name)


class Tag(models.Model):
    name = models.CharField(max_length=20, null=True)

    def __str__(self) -> str:
        return str(self.name)


class Product(models.Model):
    objects = None
    CATEGORY = (
        ("Indoor", "Indoor"),
        ("Outdoor", "Outdoor"),
    )
    name = models.CharField(max_length=20, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=20, null=True, choices=CATEGORY)
    description = models.CharField(max_length=20, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return str(self.name)


class Order(models.Model):
    objects = None
    STATUS = (
        ("Pending", "Pending"),
        ("Out for Delivery", "Out for Delivery"),
        ("Delivered", "Delivered"),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, null=True, choices=STATUS)

    def __str__(self) -> str:
        return self.product.name
