from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .forms import diff_fields_try, user_form, user_form_full
from .models import diff_field


def fun(request):
    if request.method == 'POST':
        fm = diff_fields_try(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = diff_fields_try()
    return render(request, 'index.html', {'form': fm})


def show_list(request):
    data = diff_field.objects.all()
    return render(request, 'show_list.html', {'data': data})


def edit_list(request):
    if request.method == 'POST':
        obj_edit = diff_field.objects.get(pk=id)
        fm = diff_fields_try(request.POST, instance=obj_edit)
        if fm.is_valid():
            fm.save()
    else:
        obj_edit = diff_field.objects.get(pk=id)
        fm = diff_fields_try(instance=obj_edit)
    return render(request, 'update_edit.html', {'form': fm})


def delete_list(request):
    if request.method == 'POST':
        obj_del = diff_field.objects.get(pk=id)
        obj_del.delete()
        return HttpResponseRedirect('/task_2')
    else:
        return HttpResponse("can't delete")


def check_user(request):
    check_exist = False
    if request.method == 'POST':
        user = user_form.cleaned_data['username']
        password = user_form.cleaned_data['password']
        check_exist = diff_field.objects.get(username=user, password=password)
        if check_exist:
            data = diff_field.objects.get(Name=user).all()
    else:
        data = {}
    return render(request, 'show_list.html', {'data': data})


def new_user_add(request):
    if request.method == 'POST':
        fm = user_form_full(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = user_form_full()
    return render(request, 'user_login.html', {'form': fm})
