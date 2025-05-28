from django.shortcuts import render,redirect
from students.models import Student

# 학생정보리스트
def list(request):
    qs = Student.objects.all()
    context = {'list':qs}
    return render(request,'students/list.html',context)

# 학생상세정보
def view(request,name):
    qs = Student.objects.get(name=name)
    context = {'stu':qs}
    return render(request,'students/view.html',context)

# 학생정보등록
def write(request):
    if request.method == 'POST':  # POST 방식으로 제출했을 경우
        name = request.POST.get('name')
        major = request.POST.get('major')
        grade = request.POST.get('grade')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        print('입력값 :',name,major,grade,age,gender)
        qs = Student(name=name,major=major,grade=grade,age=age,gender=gender)
        qs.save()
        return redirect('/students/list/')

    else:  # GET 방식으로 들어갔을 경우
        return render(request,'students/write.html')

# 학생정보수정
def update(request,name):
    if request.method == 'GET':  # GET 방식으로 제출했을 경우
        qs = Student.objects.get(name=name)
        context = {'stu':qs}
        return render(request,'students/update.html',context)

    else:  # POST 방식으로 들어갔을 경우
        name2 = request.POST.get('name')
        major = request.POST.get('major')
        grade = request.POST.get('grade')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        print('입력값 :',name2,major,grade,age,gender)
        
        # DB입력
        qs = Student.objects.get(name=name)
        qs.name = name2 
        qs.major = major
        qs.grade = grade
        qs.age = age
        qs.gender = gender
        qs.save()
        return redirect('/students/list/')

# 학생정보삭제
def delete(request,name):
    qs = Student.objects.get(name=name)
    qs.delete()
    return redirect('/students/list/')