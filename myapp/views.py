from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
# Create your views here.


def index(request):
    title = 'Django Course!!!'
    return render(request, 'index.html', {
        'title': title
    })


def about(request):
    username = 'henryttdev'
    return render(request, 'about.html', {
        'username': username
    })


def projects(request):
    #projects = list(Project.objects.values())
    #return JsonResponse(projects, safe=False)
    projects = Project.objects.all()
    return render(request, 'projects.html', {
        'projects': projects
    })


def tasks(request):
    # task = get_object_or_404(Task)
    #tasks = list(Task.objects.values())
    # print(tasks)
    # return JsonResponse(tasks, safe=False)
    tasks = Task.objects.all()
    print("Resultado" + str(tasks))
    return render(request, 'tasks.html', {
        'tasks': tasks
    })
   

def tasksById(request, id):
    # task = Task.objects.get(id=id)
    task = get_object_or_404(Task, id=id)
    return HttpResponse("tasks %s" % task.title)


def hello(request, username):
    print(username)
    return HttpResponse("<h1>Hello %s</h1>" % username)
