from django.urls import path
from . import views

app_name = 'student'
urlpatterns = [
    path('list/',views.list,name='list'),
    path('write/',views.write,name='write'),
    path('writeOK/',views.writeOK,name='writeOK'),
    # html -> server 1.파라미터 2.api방식 3.js
    path('view/<int:no>/',views.view,name='view'),
    path('update/<int:no>/',views.update,name='update'), # 학생정보수정페이지 열기
    path('updateOK/',views.updateOK,name='updateOK'), # 학생정보수정
    path('delete/<int:no>/',views.delete,name='delete'), # 학생정보삭제
]
