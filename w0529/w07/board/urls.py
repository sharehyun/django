from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    path('notice/',views.notice, name='notice'),
]
