from django.shortcuts import redirect


def unauthenticated_user(view_function):
    def wrapper_function(request: object, *args: object, **kwargs: object) -> object:
        if request.user.is_authenticated:
            return redirect("home")
        return view_function(request, *args, **kwargs)

    return wrapper_function
