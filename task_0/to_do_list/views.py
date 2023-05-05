from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import to_do_list_form, user_from
from .models import to_do_list_models, user
from .decorators import allowed_user
from django.contrib.auth.decorators import login_required


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            try:
                if user.groups.all()[0].name == 'admin':
                    return redirect('superuser')
                else:
                    return redirect('normyuser')
            except:
                return HttpResponse("consult the server admin")
        else:
            return render(request, 'login.html', {'message': 'User dosent exists'})
    else:
        return render(request, 'login.html')


@login_required(login_url='/')
@allowed_user(allowed_roles = ['admin'])
def superuser(request):
    info = user.objects.get(pk = request.user.id)
    return render(request, 'sup_user_actions.html', {'info': info})


@login_required(login_url='/')
@allowed_user(allowed_roles = ['admin'])
def superuser_add_list(request):
    if request.method == 'POST':
        fm = to_do_list_form(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            fm = to_do_list_form()
    else:
        fm = to_do_list_form()
    return render(request, 'add_list_to_users.html', {'form': fm})


@login_required(login_url='/')
@allowed_user(allowed_roles = ['admin'])
def task_show_suser(request):
    data = to_do_list_models.objects.all()
    return render(request, 'task_show_suser.html', {'data': data})


@login_required(login_url='/')
@allowed_user(allowed_roles = ['normy_user'])
def normyuser(request):
    info = user.objects.get(pk = request.user.id)
    data = to_do_list_models.objects.filter(assign_to=request.user)
    return render(request, 'to_do_list.html', {'data': data, 'info': info})


def sign_in(request):
    if request.method == 'POST':
        fm = user_from(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            fm = user_from()
    else:
        fm = user_from()
    return render(request, 'sign_in.html', {'form': fm})


@login_required(login_url='/')
@allowed_user(allowed_roles = ['admin'])
def delete(request, id):
    if request.method == 'POST':
        obj_del = to_do_list_models.objects.get(pk=id)
        obj_del.delete()
        return HttpResponseRedirect('/superuser/task_show_suser/')
    else:
        return HttpResponse("can't delete")


@login_required(login_url='/')
@allowed_user(allowed_roles = ['admin'])
def edit(request, id):
    if request.method == 'POST':
        obj_edit = to_do_list_models.objects.get(pk=id)
        fm = to_do_list_form(request.POST, instance=obj_edit)
        if fm.is_valid():
            fm.save()
    else:
        obj_edit = to_do_list_models.objects.get(pk=id)
        fm = to_do_list_form(instance=obj_edit)
    return render(request, 'admin_edit.html', {'form': fm})

def log_out(request):
    logout(request)
    return redirect('login_user')