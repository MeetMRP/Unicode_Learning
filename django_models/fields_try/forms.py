from django import forms

from .models import User, diff_field


class diff_fields_try(forms.ModelForm):
    class Meta:
        model = diff_field
        fields = '__all__'

class user_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class user_form_full(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'