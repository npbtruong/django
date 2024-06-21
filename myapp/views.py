from django.shortcuts import render, HttpResponse
from .models import User
# Create your views here.
# def home(request):
#     return HttpResponse('<button>Click me</button>')
def home(request):
    return render(request, 'home.html', {})

def todos(request):
    items = User.objects.all()
    return render(request, 'todos.html', {"todos": items})