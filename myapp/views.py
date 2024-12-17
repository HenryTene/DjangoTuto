from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def projects(request):
    projects = list(Project.objects.values())
   ## return JsonResponse(projects, safe=False)
    return render(request, 'projects.html')

def tasks(request):
    # task = get_object_or_404(Task)
    tasks = list(Task.objects.values())
    #print(tasks)
    #return JsonResponse(tasks, safe=False)
    return render(request, 'tasks.html')

def tasksById(request, id):
    # task = Task.objects.get(id=id)
    task = get_object_or_404(Task, id=id)
    return HttpResponse("tasks %s" % task.title)


def hello(request, username):
    print(username)
    return HttpResponse("<h1>Hello %s</h1>" % username)
