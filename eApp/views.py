from django.shortcuts import render
from .models import Cvideo


# Create your views here.

def index(request):
    return(render(request, 'eApp/index.html'))

def about(request):
    return(render(request, 'eApp/about.html', {'title' : 'About'}))


def ncertSol(request):
    clss = request.GET.get('class','')
    subb = request.GET.get('subject','')
    srch = request.GET.get('search','')
    allVid=Cvideo.objects.all()
    if srch!=None and srch.strip()!="":
        allVid = allVid.filter(title__contains=srch)
    else :
        if clss!=None and clss.strip()!="":
            allVid = allVid.filter(cls=clss)
            if subb!=None and subb.strip()!="":
                allVid = allVid.filter(sub=subb)
    context = {
        'cvid' : allVid.order_by('-id')[:10],
        'title' : ' class '+clss,
    }
    return(render(request, 'eApp/courses.html',  context))
