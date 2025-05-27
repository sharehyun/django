from django.shortcuts import render

def result(request,id,pw,name):
    context = {'id':id,'pw':pw,'name':name}
    return render(request, 'result.html', context) 