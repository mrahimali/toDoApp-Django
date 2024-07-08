from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo

# Create your views here.
def toDoList(req):
    todo=Todo.objects.order_by('-id')
    return render(req, 'todo/index.html', {'todos':todo})

def home(req):
    return HttpResponse("<h1>Home Page </h1>")

def create_todo(req):
    if req.method=='POST':
        title=req.POST.get('title')
        description=req.POST.get('desc')
        Todo.objects.create(title=title, description=description)
    return redirect('todo')

def complete_task(req, todo_id):
    todo=Todo.objects.get(id=todo_id)
    todo.completed=True
    todo.save()
    return redirect('todo')

def delete_task(req, todo_id):
    todo=Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('todo')

def edit_task(req, todo_id):
    todo=Todo.objects.get(id=todo_id)
    return render(req, 'todo/index.html', {'todo':todo})

def update_task(req, todo_id):
    todo=Todo.objects.get(id=todo_id)
    if req.method=='POST':
        todo.title=req.POST.get('title')
        todo.description=req.POST.get('desc')
        todo.save()
        return redirect('todo')


