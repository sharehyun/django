from django.shortcuts import render,redirect
from member.models import Member

def login(request):
    if request.method == 'GET':
        idCheck = request.COOKIES.get('idCheck','')
        context = {'save_id':idCheck}
        return render(request, 'member/login.html')
    
    elif request.method == 'POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        
        try: qs = Member.objects.get(id=id,pw=pw)
        except:
            context = {'msg':0}
            return render(request,'member/login.html',context)
                
        # session 저장
        request.session['session_id'] = id
        request.session['session_nickName'] = qs.nickName
        
        # response 쿠키 저장
        context = {'msg':1}
        response = render(request,'member/login.html',context)
        if idCheck != None:
            request.set_cookie('idCheck')
        
        return response