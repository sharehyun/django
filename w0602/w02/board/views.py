from django.shortcuts import render
from board.models import Board

# Create your views here.
def list(request):
    qs = Board.objects.order_by('-bno')
    context = {'list':qs}
    
    return render(request,'board/list.html',context)

def write(request):
    if request.method == 'GET':
        return render(request, 'board/write.html')
    elif request.method == 'POST':
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.POST.get('bfile')
        
        qs = Board.objects.create(id='aaa',btitle=btitle,bcontent=bcontent,bfile=bfile)
        qs.bgroup = qs.bno
        
        qs.save()
    return 