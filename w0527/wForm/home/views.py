from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def result(request):
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    name = request.POST.get('name')
    gender = request.POST.get('gender')
    hobbies = request.POST.getlist('hobby')
    
    context = {'id':id,'pw':pw,'name':name,'gender':gender,'hobby':hobbies}
    
    return render(request,'result.html',context)