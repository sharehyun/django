from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def list(request):
    # HttpResponse : 글자를 http? html?파일로 변경해서 출력 http라 쓰면서 html이라 하심 ㄷㄷ
    return HttpResponse("리스트 페이지를 오픈합니다.")
    # return render(request,'list.html')
    
def view(request):
    return HttpResponse('뷰 페이지를 오픈합니다.')

def write(request):
    return render(request,'write.html')  # html 페이지 오픈

def delete(request):
    return render(request,'delete.html')