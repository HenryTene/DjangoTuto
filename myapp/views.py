from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Index</h1>")
def hello(request, username):
    print(username)
    return HttpResponse("<h1>Hello %s</h1>" % username)
def about(request):
    return HttpResponse("<h2>About</h2>")