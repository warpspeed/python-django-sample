from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Task


def index(request):
    if (request.POST):
        task_name = request.POST["name"]
        if (task_name != ""):
            task = Task(name=task_name)
            task.save()
        return redirect('index')
    else:
        tasks = Task.objects.all()
        template = loader.get_template('taskapp/index.html')
        context = RequestContext(request, {
            'tasks': tasks,
        })
        return HttpResponse(template.render(context))


def clear_complete(request):
    if (request.POST):
        for task in Task.objects.all():
            if (task.is_complete):
                task.delete()
    return redirect('index')


def toggle_complete(request, task_id):
    if (request.POST):
        task = Task.objects.get(id=task_id)
        task.toggle_complete()
        task.save()
    return redirect('index')
