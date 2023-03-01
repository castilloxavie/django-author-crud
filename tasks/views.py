from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .form import taskForm
from .models import task
from django.utils import timezone
from django.contrib.auth.decorators import  login_required 


# Create your views here.

def home(request):
    return render(request, 'home.html',)



def signup(request):

    if request.method == "GET":
        return render(request, 'signup.html', {
            "form": UserCreationForm
        })

    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                # register user
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect("tareas")

            except IntegrityError:
                return render(request, 'signup.html', {
                    "form": UserCreationForm,
                    "error": "Username alrealy exists"
                })

        return render(request, 'signup.html', {
            "form": UserCreationForm,
            "error": "password do not match"
        })



@login_required
def tasks(request):
    tasks = task.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, "tasks.html", {"tasks": tasks})



@login_required
def tasks_complete(request):
    tasks = task.objects.filter(user=request.user, datecompleted__isnull=False ).order_by('-datecompleted')
    return render(request, "tasks.html", {"tasks": tasks})



@login_required
def create_tasks(request):

    if request.method == 'GET':
        return render(request, 'create_tasks.html', {
            "form": taskForm
        })
    else:
        try:
            form = taskForm(request.POST)
            new_tasks = form.save(commit=False)
            new_tasks.user = request.user
            new_tasks.save()
            return redirect('tareas')
        except ValueError:
            return render(request, 'create_tasks.html', {
                "form": taskForm,
                "error": "please provide valida data"
            })




@login_required
def task_detail(request, task_id):
    if request.method == 'GET':
        tasks = get_object_or_404(task, pk=task_id, user=request.user)
        form = taskForm(instance=tasks)
        return render(request, 'tasks_detail.html', {
            "task": tasks,
            "form": form
        })
    else:
        try:
            tasks = get_object_or_404(task, pk=task_id, user=request.user)
            form = taskForm(request.POST, instance=tasks)
            form.save()
            return redirect('tareas')
        except ValueError:
            return render(request, 'tasks_detail.html', {
                "task": tasks,
                "form": form,
                "errror": "Error updating task"
            })



@login_required
def complete_task(request, task_id):
    tasks = get_object_or_404(task, pk=task_id, user=request.user)
    if request.method == 'POST':
        tasks.datecompleted = timezone.now()
        tasks.save()
        return redirect('tareas')



@login_required
def delete_task(request, task_id):
    tasks = get_object_or_404(task, pk=task_id, user=request.user)
    if request.method == 'POST':
        tasks.delete()
        return redirect("tareas")



@login_required
def signout(request):
    logout(request)
    return redirect('inicio')



def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            "form": AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                "form": AuthenticationForm,
                "errror": "username or password is incorrect"
            })
        else:
            login(request, user)
            return redirect('tareas')
