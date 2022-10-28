from django.contrib import admin
from .models import user, to_do_list_models


@admin.register(user)
class New_user(admin.ModelAdmin):
    list_display = [field.name for field in user._meta.fields]


@admin.register(to_do_list_models)
class New_user(admin.ModelAdmin):
    list_display = ['assigned_to', 'task_title',
                    'description', 'related_image', 'end_date']
