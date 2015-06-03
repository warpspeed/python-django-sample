from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Task

def index(request):
    latest_task_list = Task.objects.all()
    template = loader.get_template('taskapp/index.html')
    context = RequestContext(request, {
                             'latest_task_list': latest_task_list,
                             })
    return HttpResponse(template.render(context))

def add(request):
    text = request.POST["task_text"]
    if (text != ""):
        t2 = Task(task_text=text)
        t2.save()
    return redirect('index')

def clear(request):
    if (request.POST):
        for task in Task.objects.all():
            if (task.is_complete):
                task.delete()
    return redirect('index')

def toggle_complete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.toggle_complete()
    task.save()
    return redirect('index')