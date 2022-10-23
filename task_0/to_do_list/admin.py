from django.contrib import admin
from .models import user, to_do_list_model

@admin.register(user)
class New_user(admin.ModelAdmin):
    list_display = [field.name for field in user._meta.fields]

@admin.register(to_do_list_model)
class New_user(admin.ModelAdmin):
    list_display = ['assigned_to', 'task_title', 'description', 'related_quantity', 'related_image', 'task_status', 'end_date']
