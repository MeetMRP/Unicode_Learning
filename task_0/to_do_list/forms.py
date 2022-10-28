from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import user, to_do_list_models


class user_from(UserCreationForm):
    class Meta:
        model = user
        fields = ['username', 'password1', 'profile_picture',
                  'Moblie_number', 'gender', 'is_superuser']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['password2']


class to_do_list_form(forms.ModelForm):
    class Meta:
        model = to_do_list_models
        fields = '__all__'
