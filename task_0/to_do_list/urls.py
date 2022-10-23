from django.urls import path

from . import views

urlpatterns = [
    path('', views.login_user, name='login_user'),
    path('superuser/<str:username>', views.superuser, name='superuser'),
    path('normyuser/<str:username>', views.normyuser, name='normyuser'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('superuser/task_show_suser/', views.task_show_suser, name='task_show_suser'),
    path('delete/<int:id>/', views.delete, name = 'delete'),
    path('edit/<int:id>/', views.edit, name = 'edit'),
]
