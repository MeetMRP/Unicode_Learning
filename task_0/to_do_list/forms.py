from django import forms
from django import forms
from .models import user, to_do_list_model

class user_from(forms.ModelForm):
    class Meta:
        model = user
        fields = '__all__'

class to_do_list_form(forms.ModelForm):
    class Meta:
        model = to_do_list_model
        fields = '__all__'

class user_login(forms.ModelForm):
    class Meta:
        model = user
        fields = ['username', 'password']