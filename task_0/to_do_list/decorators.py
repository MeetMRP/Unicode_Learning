from django.http import HttpResponse
from django.shortcuts import redirect, HttpResponseRedirect


def allowed_user(allowed_roles=[]):
    def allowed_user_decorator(views_function):
        def allowed_user_decorator_wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                group = None
                if request.user.groups.exists():
                    group = request.user.groups.all()[0].name
                if group in allowed_roles:
                    return views_function(request, *args, **kwargs)
                else:
                    if group == 'admin':
                        return redirect('superuser')
                    else:
                        return redirect('normyuser')
            else:
                return HttpResponse('you are not authorised')
        return allowed_user_decorator_wrapper
    return allowed_user_decorator