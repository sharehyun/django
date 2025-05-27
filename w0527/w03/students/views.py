from django.shortcuts import render

def send(request,name,age):
    print('전달받은 값 :',name,age)
    context = {'name':name,'age':age}
    return render(request,'students/send.html',context)    


def write(request):
    return render(request,'students/write.html')


def view(request):
    name = request.GET.get('name')
    age = request.GET.get('age')
    print('이름 정보 :',name)
    print('나이 정보 :',age)
    context = {"name":name,"age":age}
    return render(request,'students/view.html',context)


def list(request):
    # request -> id:aaa
    id = request.POST.get('id')  # 변수 . . . .
    pw = request.POST.get('pw')
    gender = request.POST.get('gender')
    tel = request.POST.get('tel')
    hobbys = request.POST.getlist('hobby') # 리스트
    
    print("입력된 아이디값 :",id)
    print("입력된 패스워드값 :",pw)
    print("입력된 성별 :",gender)
    print("입력된 전화번호 :",tel)
    print("입력된 취미 :",hobbys)
    context = {"id":id,"pw":pw,'gender':gender,'tel':tel,'hobby':hobbys}
    return render(request, 'students/list.html',context)
