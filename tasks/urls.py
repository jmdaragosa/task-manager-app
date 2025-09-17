from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/', views.task_list, name='task_list'),
    path('register/', views.register, name='register'),
    path('toggle/<int:task_id>/', views.toggle_task, name='toggle_task'),

    path('task/delete/<int:task_id>/', views.delete_task, name='delete_task'),
]