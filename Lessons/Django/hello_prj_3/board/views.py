from django.shortcuts import render, redirect
from .models import Board
import datetime

def index(request):
    ctx = {"msg":"welcome django"}
    return render(request,'board/index.html',ctx)

def board_create(request):
    if request.method == 'POST': # POST방식 요청?
        post_data = request.POST #입력데이터
        board = Board(
            title=post_data.get('title'),
            content=post_data.get('content'),
        )
        board.save()
        return redirect('main')
    return render(request,'board/create.html')

def board_view(request, pk):#primary key(주키-중복x 생략x)
	brd = Board.objects.get(pk=pk)
	return render(request,'board/board_view.html',{'board':brd})

def board_list(request):
    board_list = Board.objects.all().order_by('-created_at')
    ctx =  {'brd_list':board_list}
    return render(request, 'board/list.html',ctx)

def board_update(request,pk):
    if request.method == 'POST': #데이터 변경작업
        post_data = request.POST

        my_post = Board.objects.get(id=pk)
        my_post.title = post_data.get('title')        
        my_post.content = post_data.get('content')        
        my_post.updated_at = datetime.datetime.now()        
        my_post.save()
        return redirect('list')
    brd = Board.objects.get(pk=pk)
    ctx={'brd':brd}
    return render(request,'board/update.html',ctx)

def board_delete(request,pk):
    post = Board.objects.get(id=pk)
    post.delete()
    return redirect('list')
