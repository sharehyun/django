from django.urls import path,include
from . import views

app_name = 'students'
urlpatterns = [
    path('result/<str:id>/<str:pw>/<str:name>',views.result,name='result'),
]