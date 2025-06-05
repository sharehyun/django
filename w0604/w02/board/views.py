from django.shortcuts import render,redirect
from board.models import Board
from django.db.models import F,Q
from django.core.paginator import Paginator

# 게시판리스트
def list(request):
    page = int(request.GET.get('page',1))
    search = request.GET.get('search')
    category = request.GET.get('category')
    
    if search=='':  # 일반리스트로 넘어온 경우
        # 게시글 전체 가져오기
        qs = Board.objects.order_by('-bgroup','bstep')
        # 페이지 처리
        paginator = Paginator(qs,5)  # 5개씩 쪼갬
        list = paginator.get_page(page)  # 리스트에 5개씩 쪼갠 페이지 넣음
        context = {'list':list,'page':page}
        return render(request, 'board/list.html', context)
    else:  # 검색페이지로 넘어온 경우
        if category == 'all':
            qs = Board.objects.filter(Q(btitle__contains=search)|Q(bcontent__contains=search))
        elif category == 'btitle':
            qs = Board.objects.filter(btitle__contains=search)
        else:
            qs = Board.objects.filter(bcontent__contains=search)
        
        # 페이지 처리
        paginator = Paginator(qs,5)  # 5개씩 쪼갬
        list = paginator.get_page(page)  # 리스트에 5개씩 쪼갠 페이지 넣음
        context = {'list':list,'page':page}
        return render(request, 'board/list.html', context)

# 게시판작성
def write(request):
    if request.method == 'GET':
        return render(request,'board/write.html')
    
    elif request.method == 'POST':
        id = request.POST.get('id')
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.FILES.get('bfile','')  # 없으면 공백
        
        qs = Board.objects.create(id=id,btitle=btitle,bcontent=bcontent,bfile=bfile)
        qs.bgroup = qs.bno
        qs.save()
        context = {'msg':1}
        
        return render(request,'board/write.html',context)

# 글상세보기
def view(request,bno):
    qs = Board.objects.get(bno=bno)
    context = {'board':qs}
    return render(request, 'board/view.html',context)


# 게시글삭제
def delete(request,bno):
    ## 게시글삭제
    Board.objects.get(bno=bno).delete()
    return redirect('/board/list/')


# 게시글수정
def update(request,bno):
    if request.method == 'GET':
        qs = Board.objects.get(bno=bno)
        context = {'board':qs}
        return render(request,'board/update.html',context)
    elif request.method == 'POST':
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.FILES.get('bfile')
        qs = Board.objects.get(bno=bno)
        qs.btitle = btitle
        qs.bcontent = bcontent
        # qs.bfile = bfile
        qs.save()
        context = {'msg':1,'board':qs}
        return render(request,'board/update.html',context)

    
# 답글달기 - 답글달기페이지열기, 답글달기저장
def reply(request,bno):
    if request.method == 'GET':
        qs = Board.objects.get(bno=bno)
        context = {'board':qs}
        return render(request,'board/reply.html',context)
    elif request.method == 'POST':
        id = request.POST.get("id") #session_id 가져옴.
        bgroup = request.POST.get("bgroup")  # 부모의 bgroup
        bstep = int(request.POST.get("bstep")) # 부모의 bstep
        bindent = int(request.POST.get("bindent")) #부모의 bindent
        btitle = request.POST.get("btitle")
        bcontent = request.POST.get("bcontent")
        bfile = request.POST.get("bfile")
        
        ### 답글달기저장
        # 1.  gt, lt, gte, lte 언더바 2개 넣어야 함.
        # 부모보다 bstep 더 큰것, 모든자식들은 전부 bstep을 1씩 증가시켜야 함.
        # F함수 현재 찾아진 컬럼의 값을 모두 가져옴.
        reply_qs = Board.objects.filter(bgroup=bgroup,bstep__gt=bstep)
        reply_qs.update(bstep = F('bstep')+1)
        # 2. db저장
        qs = Board.objects.create(id=id,btitle=btitle,bcontent=bcontent,
            bgroup=bgroup,bstep=bstep+1,bindent=bindent+1,bfile=bfile)
        print('')        
        context = {"msg":1,'board':qs}
        return render(request,'board/reply.html',context)