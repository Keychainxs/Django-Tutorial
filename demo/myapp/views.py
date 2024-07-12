from django.shortcuts import render, HttpResponse
from .models import TodoItem
# Create your views here.
def index(request): 
    return render(request, 'index.html')

def toDo(request): 
    items = TodoItem.objects.all()
    return render(request, 'toDos.html', {"toDos": items})