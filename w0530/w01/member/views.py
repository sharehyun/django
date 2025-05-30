from django.shortcuts import render,redirect
from member.models import Member

# 로그인 페이지 - GET, 로그인 확인 - POST
def login(request):
    if request.method =='GET': # 로그인페이지 연결
        return render(request,'member/login.html')
    
    elif request.method == 'POST':  # 로그인 확인 클릭
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        print('아이디, 패스워드 :',id,pw)
        # id.pw가 있는지 확인
        try: 
            qs = Member.objects.get(id=id)
            if qs.pw == pw:
                request.session['session_id'] = id  # session 할당
                txt = 1
            else:
                txt = -1 # 아이디 O, 패스워드 일치X
        except:
            txt = 0  # 아이디 X, 회원가입 진행 
        
        # try: 
        #     qs = Member.objects.get(id=id)
        #     request.session['session_id'] = id  # session 할당
        #     txt = 1  # 성공
        # except:
        #     txt = 0  # 실패
        
        print(txt)
        
        context = {'msg':txt}
        return render(request,'member/login.html',context)
        # return redirect('/')


def logout(request):
    request.session.clear()  # 세션 모두 삭제, del request.session['session_id']
    # del request.session['session_id']  # session 1개 삭제
    context = {'msg':2}
    return render(request,'member/login.html',context)