#coding:utf-8
from django.http import HttpResponse,HttpResonseRedirect
from django.shortcuts import render

# Create your views here.

def index(request):
    return  HttpResponse("hello world")

def detail(request, p1):
    return  HttpResponse(p1)

def getTest1(request):
    return render(request,'booktest/getTest1.html')

def getTest2(request):
    a1 = request.GET['a']
    b1 = request.GET['b']
    c1 = request.GET['c']

    context = {'a':a1,'b':b1,'c':c1}
    
    return render(request,'booktest/getTest2.html',context)

def getTest3(request):
    a1 = request.GET.getlist('a')
    context={'a':a1}
    return render(request,'booktest/getTest3.html',context)

def postTest1(request):
    return render(request,'booktest/postTest1.html')

def postTest2(request):
    uname=request.POST['uname']
    upwd=request.POST['upwd']
    ugender=request.POST.get('ugender')
    uhobby=request.POST.getlist('uhobby')
    context={'uname':uname,'upwd':upwd,'ugender':ugender,'uhobby':uhobby}
    return render(request,'booktest/postTest2.html', context)

def cookieTest(request):
    cookie= request.COOKIES
    if cookie.has_key('t1'):
        reponse.write(cookie['t1'])
    response = HttpResponse()
#    response.set_cookie('ti','abc')

    return response

def redtest1(request):
    return HttpResopnseRedirect('/booktest/redtest2')


def redtest2(request):
    return HttpReponse('redirct')
    

def session1(request):
    uname=request.session.get('myname','none')
    context={'uname',uname}
    return render(rquest,'booktest/session1.html',context)

def session2(request):
    return render(request,'booktest/session2.html')

def session2_handle(request):
    uname = request.POST['uname']
    request.session['myname']=uname
    request.session.set_expiry(0)
    return redirect('/booktest/session1/')

def session3(request):
    del request.session['myname']
    return redirect('/booktest/session1/')
