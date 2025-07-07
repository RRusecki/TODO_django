from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template.context_processors import request
from django.contrib import messages
from .forms import TaskForm
from .models import Task

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "todo/task_list.html", {"tasks": tasks})

@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("task_list")
    else:
        form = TaskForm()
    return render(request, "todo/task_form.html", {"form": form})

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect(("task_list"))
    else:
        form = TaskForm(instance=task)
    return render(request, "todo/task_form.html", {"form": form})

@login_required
def delete_task(request,task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == "POST":
        task.delete()
        messages.success(request, "Užduotis ištrinta sėkmingai.")
        return redirect("task_list")
    return render(request, "todo/confirm_delete.html", {"task": task})