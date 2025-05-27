from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse('확인')
    return render(request,'index.html')

def result(request):
    name = request.POST.get('name')
    kor = request.POST.get('kor')
    eng = request.POST.get('eng')
    total = int(kor)+int(eng)  # 타입변경 -> 합계 계산
    hobbys = request.POST.getlist('hobby')
    context = {'name':name,'kor':kor,'eng':eng,'total':total,'hobby':hobbys}
    return render(request,'result.html',context)