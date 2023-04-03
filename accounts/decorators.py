from django.shortcuts import redirect
from django.http import HttpResponse


def unauthenticated_user(view_function):
    def wrapper_function(request: object, *args: object, **kwargs: object) -> object:
        if request.user.is_authenticated:
            return redirect("home")
        return view_function(request, *args, **kwargs)

    return wrapper_function


def allowed_users(allowed_users=[]):
    def decorator(view_function):
        def wrapper_function(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_users:
                return view_function(request, *args, **kwargs)
            else:
                return HttpResponse("You are nothing but a cutie")

        return wrapper_function

    return decorator


def allow_admin_user(view_function):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == "admin":
            return view_function(request, *args, **kwargs)
        else:
            return redirect("user-page")

    return wrapper_function
