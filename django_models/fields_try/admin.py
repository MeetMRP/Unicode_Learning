from django.contrib import admin
from .models import diff_field, name, User


@admin.register(diff_field)
class reg_admin(admin.ModelAdmin):
    list_display = [field.name for field in diff_field._meta.fields]


@admin.register(name)
class reg_admin(admin.ModelAdmin):
    list_display = [field.name for field in name._meta.fields]


@admin.register(User)
class New_user(admin.ModelAdmin):
    list_display = [field.name for field in User._meta.fields]
