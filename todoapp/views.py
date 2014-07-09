from todoapp.models import Task
from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.


def next_view(request, user_id):
    task_dict = user_task(user_id)
    return render(request, "user_task.html", task_dict)
    #task_data = Task.objects.filter(user_id=user_id)
    #public_data = Task.objects.filter(task_priority=1)
    #return render(request, "user_task.html", {"task_data": task_data, "public_data": public_data})


def user_task(user_id):
    task_data = Task.objects.filter(user_id=user_id)
    public_data = Task.objects.filter(task_priority=1).exclude(user_id=user_id)
    print "\n\n", public_data.count()
    data_dict = {"task_data": task_data, "public_data": public_data}
    return data_dict


def all_task(request):
    task_data = get_task_data()
    return render(request, "all_task.html", {"task_data": task_data})


def get_task_data():
    return Task.objects.all()
