from django.shortcuts import render
from .forms import diff_fields_try


def fun(request):
    if request.method == 'POST':
        fm = diff_fields_try(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = diff_fields_try()
    return render(request, 'index.html', {'form': fm})
