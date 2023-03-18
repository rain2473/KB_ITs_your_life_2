from django.shortcuts import render, redirect
from .models import Todo
import datetime

def index(request):
    ctx = {"msg":"todo list"}
    return render(request,'todo/index.html',ctx)

def todo_create(request):
    if request.method == 'POST': # POST방식 요청?
        post_data = request.POST #입력데이터
        todo = Todo(
            title=post_data.get('title'),
            content=post_data.get('content'),
        )
        todo.save()
        return redirect('main')
    return render(request,'todo/create.html')

def todo_view(request, pk):#primary key(주키-중복x 생략x)
	brd = Todo.objects.get(pk=pk)
	return render(request,'todo/todo_view.html',{'todo':brd})

def todo_list(request):
    todo_list = Todo.objects.all().order_by('-created_at')
    ctx =  {'brd_list':todo_list}
    return render(request, 'todo/list.html',ctx)

def todo_update(request,pk):
    if request.method == 'POST': #데이터 변경작업
        post_data = request.POST

        my_post = Todo.objects.get(id=pk)
        my_post.title = post_data.get('title')        
        my_post.content = post_data.get('content')        
        my_post.updated_at = datetime.datetime.now()        
        my_post.save()
        return redirect('list')
    brd = Todo.objects.get(pk=pk)
    ctx={'brd':brd}
    return render(request,'todo/update.html',ctx)

def todo_delete(request,pk):
    post = Todo.objects.get(id=pk)
    post.delete()
    return redirect('list')

def todo_detail(request,pk):
    brd = Todo.objects.get(id=pk)
    ctx =  {'brd':brd}
    return render(request, 'todo/detail.html',ctx)