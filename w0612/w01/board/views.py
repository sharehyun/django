from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.core import serializers  # json타입
from django.views.decorators.csrf import csrf_exempt
from board.models import Board


# form 게시판 - get, post
def list(request):
    qs = Board.objects.all().order_by('-ntchk','-bgroup','-bstep')
    context = {"list":qs}  # html전달
    return render(request,'board/list.html',context)
