from django.http import HttpResponse, HttpResponseForbidden

from .models import Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.shortcuts import get_object_or_404

@login_required
def home(request):
    return render(request, "tasks/home.html")

@login_required
def task_list(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        deadline = request.POST.get("deadline")

        if title:
            Task.objects.create(
                owner = request.user,
                title = title,
                description = description,
                deadline = deadline
            )
        return redirect("task_list")
    tasks = Task.objects.filter(owner=request.user).order_by("-deadline")
    return render(request, "tasks/task_list.html", {"tasks": tasks})

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

@login_required
def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, owner=request.user)
    if request.method == "POST":
        task.completed = not task.completed
        task.save()
    return  redirect('task_list')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, owner=request.user)

    if request.method == "POST":
        task.delete()
        return redirect("task_list")
    else:
        return HttpResponseForbidden('Not allowed.')