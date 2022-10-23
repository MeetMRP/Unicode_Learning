from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from .forms import to_do_list_form, user_from, user_login
from .models import to_do_list_model, user


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser == True:
                return redirect('superuser')
            else:
                return redirect('normyuser', {'username':username})
        else:
            return HttpResponse('add user')
    else:
        fm = user_login()
        return render(request, 'login.html', {'form': fm})


def superuser(request):
    if request.method == 'POST':
        fm = to_do_list_form(request.POST)
        if fm.is_valid():
            fm.save()
            fm = to_do_list_form()
    else:
        fm = to_do_list_form()
    return render(request, 'add_list_to_users.html', {'form': fm})


def normyuser(request):
    data = to_do_list_model.objects.filter(username=username)
    return render(request, 'to_do_list.html', {'data': data})


def sign_in(request):
    if request.method == 'POST':
        fm = user_from(request.POST)
        if fm.is_valid():
            fm.save()
            fm = user_from()
    else:
        fm = user_from()
    return render(request, 'sign_in.html', {'form': fm})
