from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import user, to_do_list_model

class user_from(UserCreationForm):
    class Meta:
        model = user
        fields = '__all__'

class to_do_list_form(forms.ModelForm):
    class Meta:
        model = to_do_list_model
        fields = '__all__'