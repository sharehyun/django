from django.shortcuts import render

# ajax전송에 필요한 선언
from django.http import JsonResponse

# 4. ajax전송방식 - get, post
def view2(request):
    # html에서 데이터 전달받음
    id = request.POST.get('id','')
    name = request.POST.get('name','')
    # QuerySet, QueryList도 list타입으로 변경해줘야 함 (언어가 다를 때 문제가 생김 javascript-python)
    # models db데이터가 있으면, list타입으로 변경후 전송해야 함.
    
    # 데이터 html로 전송
    context = {'id':id,'name':name,'result':'success','pw':'1111'}
    return JsonResponse(context)

# 1. form 데이터 전송 - get,post
def view(request):
    # html에서 데이터 전달받음
    id = request.POST.get('id','')
    name = request.POST.get('name','')
    # 데이터 html로 전송
    context = {'id':id,'name':name}
    return render(request,'board/view.html',context)

def list(request):
    return render(request,'board/list.html')