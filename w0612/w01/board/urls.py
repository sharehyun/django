from django.urls import path,include
from . import views

app_name = 'board'
urlpatterns = [
    # form 파라미터 형태
    path('list/',views.list,name='list'),

]
