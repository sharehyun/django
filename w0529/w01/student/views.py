from django.shortcuts import render,redirect
from student.models import Student

def delete(request,no):
    Student.objects.get(no=no).delete()
    return redirect('/student/list/')
    # return redirect('student:list')

# 학생정보수정완료
def updateOK(request):
    no = request.POST.get('no')
    qs = Student.objects.get(no=no)  # 데이터 검색
    # 데이터 수정
    qs.name = request.POST.get('name')
    qs.major = request.POST.get('major')
    qs.grade = request.POST.get('grade')
    qs.age = request.POST.get('age')
    qs.gender = request.POST.get('gender')
    hobby = request.POST.getlist('hobby')
    hobby = ','.join(hobby)
    qs.hobby = hobby
    qs.save()
    return redirect(f'/student/view/{no}/')

# 학생정보수정페이지 열기
def update(request,no):
    qs = Student.objects.get(no=no)  # set타입 1개
    context={'stu':qs}
    # qs = Student.objects.filter(no=no)  # 데이터 타입 - 리스트
    # context={'stu':qs[0]}               # 에러 X, None 데이터 넘겨짐
    return render(request, 'student/update.html',context)

def view(request,no):
    try: 
        qs = Student.objects.get(no=no)
    except: qs= None
    context={'stu':qs}
    return render(request,'student/view.html',context)


# 학생정보저장
def writeOK(request):
    name = request.POST.get('name')
    major = request.POST.get('major')
    grade = request.POST.get('grade')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    hobby = request.POST.getlist('hobby')
    # 리스트타입->str타입으로 변경
    hobby = ','.join(hobby)
    
    Student(name=name,major=major,grade=grade,age=age,gender=gender,hobby=hobby,memo='등록합니다.').save()
    
    return redirect('/student/list/')

# 학생정보등록페이지 열기
def write(request):
        return render(request, 'student/write.html')

# 학생정보리스트
def list(request):
    qs = Student.objects.all()
    context = {'list':qs}
    return render(request, 'student/list.html',context)
