from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("customer/<str:pk>", views.customer),
    path("products/", views.products),
]
