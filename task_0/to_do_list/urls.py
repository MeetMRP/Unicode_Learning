from django.urls import path

from . import views

urlpatterns = [
    path('', views.login_user, name='login_user'),
    path('superuser/<int:id>', views.superuser, name='superuser'),
    path('superuser/task_show_suser/',views.task_show_suser, name='task_show_suser'),
    path('superuser/superuser_add_list/',views.superuser_add_list, name='superuser_add_list'),
    path('normyuser/<int:id>', views.normyuser, name='normyuser'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('logout', views.log_out, name='log_out'),
]
