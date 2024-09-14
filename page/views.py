from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import mail
from django.contrib.auth import authenticate,login,logout
from uuid import getnode as getmac
from .forms import *
from .models import *

NAME="Shop"
x=5

AD=ADModel.objects.all()

main_dec={
    "name": NAME,
    "ad":AD,
    "clear":False,
}

def del_mac_user(mac: int):
    print(8)
    for i in UserModel.objects.all():
        lis=i.macs[1:-1].split(',')[:-1]
        print(lis)
        if str(mac) in lis:
            lis.remove(str(mac))
        mymac='['
        for j in lis:
            mymac+=str(j)+','
        mymac+=']'
        i.macs=mymac
        i.save()

def getuser():
    for i in UserModel.objects.all():
        if str(getmac()) in i.macs:
            return i
    return None

def home(req):
    global x,AD
    AD=ADModel.objects.all()
    if 'left' in req.POST:
        form1=Form1(req.POST)
        if form1.is_valid():
            x-=1
    if 'right' in req.POST:
        form1=Form1(req.POST)
        if form1.is_valid():
            x+=1
    else:
        form1=Form1()

    x=len(VIP.objects.all())
    dec={
        "form1" : form1,
        "vip" : VIP.objects.all(),
        "x" : x,
    }

    return render(req,"home.html",{**dec,**main_dec})

def ajnas(req):
    dec={
        "ajnas": KafshModel.objects.all(),
    }
    return render(req,"ajnas.html",{**dec,**main_dec,'clear':True})

def jens(req,code):
    kafsh=KafshModel.objects.all()[int(code)-1]
    dec={
        "code":code,
        "kafsh":kafsh,
        "emtiaz":str(randint(26,50)/10)[:3],
    }
    return render(req,"jens.html",{**dec,**main_dec})

def buy(req,code):
    k=KafshModel.objects.all()[int(code)-1]
    user=getuser()
    if user:
        user.sabad=str(user.sabad)[:-1]+'\''+str(k.model)+'_'+str(k.size)+'_'+str(k.color)+'_'+str(k.price)+'\''+', '+']'
        user.save()
    else:
        return redirect('sabt')
    return redirect("factor")

def factor(req):
    user=getuser()
    if user:
        dec={
            'sabad':list( map(lambda a:a.split('_'),eval(user.sabad)) ),
            }
        return render(req,"factor.html",{**dec,**main_dec})
    else:
        return redirect("sabt")

def pardakht(req):
    user=getuser()
    if user:
        user.sabad='[]'
        user.save()
        return redirect('factor')
    else:
        return redirect('sabt')

def text(req):
    dec={
    }
    return render(req,"text.html",{**dec,**main_dec})

def callme(req):
    return render(req,"call.html",{**main_dec})

def aboutme(req):
    return render(req,"about.html",{**main_dec})

def login(req):
    error=False
    if 'sabt' in req.POST:
        form=Form3(req.POST)
        if form.is_valid():
            for i in UserModel.objects.all():
                if i.username==str(form.cleaned_data['username']) and i.password==str(form.cleaned_data['password']):
                    error=False
                    if str(getmac()) not in i.macs:
                        del_mac_user(getmac())
                        i.macs=i.macs[:-1]+str(getmac())+',]'
                        i.save()
                    return redirect("home")
            else:
                error=True
    else:
        form=Form3()
    dec={
        'form3': form,
        'error': error,
    }
    return render(req,"login.html",{**dec,**main_dec})

def signin(req):
    if "sabt" in req.POST:
        form=Form2(req.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            UserModel.objects.create(username=username,email=email,password=password)
            mail.send_mail("Hi!","this message is of Ayandegan! i am programming python!","mjsalemimj@gmail.com",[email,])
            return redirect("login")
    else:
        form=Form2()

    dec={
        "form2":form,
    }

    return render(req,"sabt.html",{**dec,**main_dec})