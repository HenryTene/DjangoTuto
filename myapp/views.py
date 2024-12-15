from django.http import HttpResponse, JsonResponse
from .models import Project,Task
from django.shortcuts import get_object_or_404, render, redirect
# Create your views here.


def index(request):
    return HttpResponse("<h1>Index</h1>")


def hello(request, username):
    print(username)
    return HttpResponse("<h1>Hello %s</h1>" % username)


def about(request):
    return HttpResponse("<h2>About</h2>")


def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)


def tasks(request):    
    #task = get_object_or_404(Task)
    tasks = list(Task.objects.values())
    print(tasks)
    return JsonResponse(tasks, safe=False)
def tasksById(request, id):
    #task = Task.objects.get(id=id)
    task = get_object_or_404(Task, id=id)
    return HttpResponse("tasks %s" % task.title)
