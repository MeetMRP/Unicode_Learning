from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .forms import to_do_list_form, user_from, user_login
from .models import to_do_list_model, user


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(user)
        print(user.is_superuser)
        if user is not None:
            #login(request, user)
            if user.is_superuser:
                return redirect('superuser', {'username':username})
            else:
                return redirect('normyuser', {'username':username})
        else:
            return HttpResponse('add user')
    else:
        fm = user_login()
        return render(request, 'login.html', {'form': fm})


def superuser(request, username):
    if request.method == 'POST':
        fm = to_do_list_form(request.POST)
        if fm.is_valid():
            fm.save()
            fm = to_do_list_form()
    else:
        fm = to_do_list_form()
    return render(request, 'add_list_to_users.html', {'form': fm})


def normyuser(request, username):
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

def task_show_suser(request):
    data = to_do_list_model.objects.all()
    return render(request, 'task_show_suser.html', {'data':data})

def delete(request, id):
    if request.method == 'POST':
        obj_del = to_do_list_model.objects.get(pk = id)
        obj_del.delete()
        return HttpResponseRedirect('/superuser/task_show_suser/')
    else:
        return HttpResponse("can't delete")

def edit(request, id):
    if request.method == 'POST':
        obj_edit = to_do_list_model.objects.get(pk = id)
        fm = to_do_list_form(request.POST, instance = obj_edit)
        if fm.is_valid():
            fm.save()
    else:
        obj_edit = to_do_list_model.objects.get(pk = id)
        fm = to_do_list_form(instance = obj_edit)
    return render(request, 'admin_edit.html', {'form' : fm})
