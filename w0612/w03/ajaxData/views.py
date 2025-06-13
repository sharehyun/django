from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.db.models import F,Q
from django.http import JsonResponse
from board.models import Board
from django.core import serializers  # json타입

# bwrite 글쓰기 - 1. ajax 데이터전송유무 2. ... db추가 4. 
def bwrite(request):
    id = request.POST.get('id')
    btitle = request.POST.get('btitle')
    bcontent = request.POST.get('bcontent') 
    print('html에서 서버측으로 전달데이터 :',id,btitle,bcontent)
    # db저장
    qs = Board.objects.create(id=id,btitle=btitle,bcontent=bcontent)
    qs.bgroup = qs.bno
    qs.save()
    
    # json타입변환
    l_qs = list(Board.objects.filter(bno=qs.bno).values())
    print(l_qs)
    
    context = {'result':"성공",'board':l_qs}
    return JsonResponse(context)

# ajax3 - Board 모든 데이터 가져오기
def ajax3(request):
    qs = Board.objects.all().order_by('-ntchk','-bgroup','bstep')
    print(qs)
    a = request.POST.get('sampleID')
    print("넘어온 데이터 :",a)
    list_qs = serializers.serialize('json',qs)
    print('변경타입 :',list_qs)
    context = {'result':"성공",'list':list_qs}
    return JsonResponse(context)

def list3(request):
    qs = Board.objects.all().order_by('-ntchk','-bgroup','bstep')
    context = {'list':qs}
    return render(request,'board/list3.html',context)

