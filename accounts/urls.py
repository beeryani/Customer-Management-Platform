from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.registerUser, name="register"),
    path("login/", views.loginUser, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("", views.home, name="home"),
    path("user/", views.userView, name="user-page"),
    path("account/", views.accountSettings, name="account"),
    path("customer/<str:pk>", views.customer, name="customer"),
    path("products/", views.products, name="products"),
    path("create_order/<str:pk>", views.createOrder, name="create_order"),
    path("update_order/<str:pk>", views.updateOrder, name="update_order"),
    path("delete_order/<str:pk>", views.deleteOrder, name="delete_order"),
    path("create_customer/", views.createCustomer, name="create_customer"),
    path("update_customer/<str:pk>", views.updateCustomer, name="update_customer"),
    path("delete_customer/<str:pk>", views.deleteCustomer, name="delete_customer"),
]
