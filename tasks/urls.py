from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/', views.task_list, name='task_list'),
    path('register/', views.register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('toggle/<int:task_id>/', views.toggle_task, name='toggle_task'),

    path('task/delete/<int:task_id>/', views.delete_task, name='delete_task'),
]