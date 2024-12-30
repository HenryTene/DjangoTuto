from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject
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
    # projects = list(Project.objects.values())
    # return JsonResponse(projects, safe=False)
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'projects': projects
    })


def tasks(request):
    # task = get_object_or_404(Task)
    # tasks = list(Task.objects.values())
    # print(tasks)
    # return JsonResponse(tasks, safe=False)
    tasks = Task.objects.all()
    print("Resultado" + str(tasks))
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })


def tasksById(request, id):
    # task = Task.objects.get(id=id)
    task = get_object_or_404(Task, id=id)
    return HttpResponse("tasks %s" % task.title)


def hello(request, username):
    print(username)
    return HttpResponse("<h1>Hello %s</h1>" % username)


def create_task(request):
    if request.method == 'GET':
        # return HttpResponse('agregando tarea')
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(title=request.POST['title'],
                            description=request.POST['description'], project_id=2)
        return redirect('tasks')


def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'projects/detail.html', {
        'project': project,
        'tasks': tasks
    })