from django.urls import path

from . import views

urlpatterns = [
    path('', views.login_user, name='login_user'),
    path('superuser/', views.superuser, name='superuser'),
    path('normyuser/', views.normyuser, name='normyuser'),
    path('sign_in/', views.sign_in, name='sign_in'),
]
