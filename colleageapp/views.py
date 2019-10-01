from django.shortcuts import render

from .models import faculty1,student1
import random
from django import template
from random import randint
from django.core.mail import send_mail
from django.db.models import Q


def fun1(request):
    return render(request,'href.html')


def fun2(request):
    return render(request,'faculty.html')

def fun3(request):
    return render(request,'student.html')


def fun4(request):
    if request.method=="POST":
        g1=request.POST['nm']
        g2=request.POST['su']
        g3=request.POST['de']
        g4=request.POST['qu']
        g5=request.POST['ex']
        g6=request.POST['em']
        sd=faculty1(name=g1,subject=g2, department=g3,qualificaton=g4,experience=g5,email=g6)
        sd.save()
        return render(request,'href.html')


def fun5(request):
    if request.method=="POST":
        c1=request.POST['ne']
        c2=request.POST['br']
        c3=request.POST['ye']
        c4=request.POST['em']
        c5=randint(1200,1500)
        dd=student1(name=c1,branch=c2,year=c3,semail=c4, unquieid=c5)
        dd.save()
        sub='userid'
        msg=str(c5)
        dg=str(c4)
        send_mail(sub,msg,'sayypureddysairam@gmail.com',[dg])
        return render(request,'href.html')

def fun6(request):
    return render(request,'faclogin.html')


def fun7(request):
    return render(request,'stulogin.html')

def fun8(request):
    if request.method=="POST":
        c1=request.POST['us']
        c2=request.POST['br']
        if student1.objects.filter(Q(unquieid=c1) & Q(branch=c2)):
            return render(request,'home.html')
    return render(request,'test.html')

def fun9(request):
    if request.method=="POST":
        gh=request.POST['dep']
        if gh=="eee" or "ece" or "mech" or "cse":
            return render(request,'depinfo.html')
    return render(request,'home.html')


def fun10(request):
    if request.method=="POST":
        gg=request.POST['eve']
        if gg=="culture" or "sports" or "dance" or "music":
            return render(request,'eventinfo.html')
    return render(request,'home.html')


def fun11(request):
    if request.method=="POST":
        kk=request.POST['fi']
        nm=faculty1.objects.get(department='kk')
        return render(request,'fac.html',{"gh":nm})

    




