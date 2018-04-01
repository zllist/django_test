from django.shortcuts import render
from models import *
from django.http import HttpResponse

# Create your views here.


def index(request):
    hero=HeroInfo.objects.get(pk=1)
    #list1=HeroInfo.objects.all()
    list1=HeroInfo.objects.filter(isDelete=False)
    context={'hero':hero,'list1':list1}
    return render(request,'booktest/index.html',context)

def show(request , id):
    context={'id':id}
    return render(request,'booktest/show.html',context)

def index2(request):
   return render(request,'booktest/index2.html') 


def user2(request):
    return render(request,'booktest/user2.html')

def user1(request):
    context={'uname':'zl'}
    return render(request,'booktest/user1.html',context)
    
def htmlTest(request):
    context={'t1':'<h1>123</h1>'}
    return render(request,'booktest/htmlTest.html',context)

def csrf1(request):
    return render(request,'booktest/csrf1.html')

def csrf2(request):
    uname=request.POST["uname"]
    return HttpResponse(uname)

def verifyCode(request):
    from PIL import Image,ImageDraw,ImageFont
    import random

    bgColor=(random.randrange(50,100),random.randrange(50,100),0)
    width=100
    height=25
    image=Image.new('RGB',(width,height),bgColor)
    font=ImageFont.truetype('FreeMono.ttf',24)
    draw=ImageDraw.Draw(image)
    text='0123ABCD'
    textTemp=''
    for i in range(4):
        textTemp1=text[random.randrange(0,len(text))]
        textTemp+=textTemp1
        draw.text((i*25,0),
            textTemp1,      
            (255, 255, 255),
            font)           
        request.session['code']=textTemp
        import cStringIO
        buf=cStringIO.StringIO()
        image.save(buf,'png')
        return HttpResponse(buf.getvalue(),'image/png')


def verifyTest1(request):
    return render(request,'booktest/verifyTest1.html')

def verifyTest2(request):        
    code1=request.POST['code1']  
    code2=request.session['code']
    if code1==code2:             
        return HttpResponse("ok")
    else:                        
        return HttpResponse("no")
































