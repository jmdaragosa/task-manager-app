from .models import Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login

@login_required
def home(request):
    return render(request, "tasks/home.html")

@login_required
def task_list(request):
    tasks = Task.objects.filter(owner=request.user)
    return render(request, "tasks/task_list.html", {'tasks': tasks})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {'form': form})