from django.urls import path,include
from . import views

# app_name 설정
app_name=''  # 아무것도 들어온 게 없을 때

urlpatterns = [
    path('',views.home,name='home'),
]
