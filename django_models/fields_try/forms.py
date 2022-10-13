from django import forms

from .models import diff_field


class diff_fields_try(forms.ModelForm):
    class Meta:
        model = diff_field
        fields = '__all__'