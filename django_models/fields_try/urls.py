from django.urls import path
from . import views

urlpatterns = [
    path('add_task/', views.fun),
    #path('show/', views.show_list),
    path('', views.check_user, name = 'check_user'),
    path('edit/', views.edit_list, name='edit'),
    path('delete/', views.delete_list, name='delete'),
    path('new_user/', views.new_user_add),
]
