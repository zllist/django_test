#coding=utf-8
from django.shortcuts import render
from django.db.models import Max
from models import *

# Create your views here.


def index(request):
    list1=BookInfo.books1.filter(heroinfo__hcontent__contains='八')
    list2 = BookInfo.books1.aggregate(Max('id')) 
    context={'list1':list1,'list2':list2}
    return render(request,'booktest/index.html', context)
