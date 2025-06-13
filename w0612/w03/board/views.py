from django.shortcuts import render,redirect
from django.http import JsonResponse
from board.models import Board
from django.core import serializers  # json타입

# ajaxWrite 글쓰기
def ajaxWrite(request):
    id = request.POST.get('id')
    btitle = request.POST.get('btitle')
    bcontent = request.POST.get('bcontent') 
    print('html에서 서버측으로 전달데이터 :',id,btitle,bcontent)
    # db저장
    qs = Board.objects.create(id=id,btitle=btitle,bcontent=bcontent)
    qs.bgroup = qs.bno
    qs.save()
    # json데이터변환, serializers, list()
    # list()타입으로 변환부분
    
    l_qs = list(Board.objects.filter(bno=qs.bno).values())
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


#----------------------------------------------------------------

# url api
def view2(request,bno):
    qs = Board.objects.get(bno=bno)
    context = {'board':qs}
    return render(request,'board/view2.html',context)

# form - get,post
def list2(request):
    if request.method == 'GET':
        qs = Board.objects.all().order_by('-ntchk','-bgroup','bstep')
        context = {'list':qs}
        return render(request,'board/list2.html',context)
    elif request.method == 'POST':
        return render(request,'board/list2.html')

#----------------------------------------------------------------


# 
def view(request):
    bno = request.GET.get('bno')
    print('bno : ',bno)
    qs = Board.objects.get(bno=bno)
    context = {'board':qs}
    return render(request, 'board/view.html',context)


# form 게시판 - get, post
def list(request):
    if request.method == 'GET':
        qs = Board.objects.all().order_by('-ntchk','-bgroup','bstep')
        context = {'list':qs}
        return render(request,'board/list.html',context)
    elif request.method == 'POST':
        id = request.POST.get('id')
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        print('넘어온 데이터 :',id,btitle,bcontent)
        
        # db저장
        qs = Board.objects.create(id=id,btitle=btitle,bcontent=bcontent)
        qs.bgroup = qs.bno
        qs.save()
        
        return redirect('/board/list/')
