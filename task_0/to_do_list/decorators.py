from django.http import HttpResponse
from django.shortcuts import redirect, HttpResponseRedirect


def right_user(views_function):
    def right_user_wrapper(request, *args, **kwargs):
        if request.user.id != id:
            print(id)
            return HttpResponseRedirect('../')
        else:
            return views_function(request, *args, **kwargs)
    return right_user_wrapper

def unauthenticated_user(views_function):
    def unauthenticated_user_wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return views_function(request, *args, **kwargs)
            else:
                return views_function(request, *args, **kwargs)
        else:
            return redirect('login_user')
    return unauthenticated_user_wrapper

def allowed_user(allowed_roles = []):
    def allowed_user_decorator(views_function):
        def allowed_user_decorator_wrapper(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return views_function(request, *args, **kwargs)
            else:
                return HttpResponse("You are not authenticated to this page")
        return allowed_user_decorator_wrapper
    return allowed_user_decorator
