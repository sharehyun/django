from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.core import serializers #json타입
from django.views.decorators.csrf import csrf_exempt #csrf토큰이 없을때 예외처리
from board.models import Board

# 게시글 삭제
def bdelete(request):
    # db삭제
    bno = request.POST.get(bno)
    Board.objects.get(bno=bno).delete()
    context = {'result':'success'}
    return JsonResponse(context)

# 게시글 등록
def bwrite(request):
    id = request.POST.get('id')
    btitle = request.POST.get('btitle')
    bcontent = request.POST.get('bcontent')
    # db저장
    qs = Board.objects.create(id=id,btitle=btitle,bcontent=bcontent)
    qs.bgroup = qs.bno
    qs.save()
    # json타입변환
    l_qs = list(Board.objects.filter(bno=qs.bno).values)
    context = {'result':'success','board':l_qs}
    return JsonResponse(context)

# form 게시판 - get, post
def blist(request):
    ### db게시글 전체가져오기
    qs =  Board.objects.all().order_by('-ntchk','-bgroup','bstep')
    print("이전데이터 :",qs)
    
    ### json타입으로 변경(Queryset -> list)
    l_qs = list(qs.values())
    print('리스트타입 :',l_qs)
    
    context = {"result":"success",'list':l_qs}
    return JsonResponse(context)
