from django.shortcuts import render
from board.models import Board

# 게시판리스트
def list(request):
    qs = Board.objects.all()
    context = {'list':qs}
    return render(request, 'board/list.html', context)

# 게시판작성
def write(request):
    if request.method == 'GET':
        return render(request,'board/write.html')
    
    elif request.method == 'POST':
        id = request.POST.get('id')
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.POST.get('bfile')
        
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


# delete,update,reply 추가 필요