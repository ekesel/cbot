
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from covid_india import states
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import os
from bs4 import BeautifulSoup as BS

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        replies = request.POST.get('reply')
        request.session['first_reply'] = replies
        if replies == 'A' or replies == 'a':
            return redirect(phaseA)
        elif replies == 'B' or replies == 'b':
            return redirect(phaseB)
        elif replies == 'C' or replies == 'c':
            return redirect(phaseC)
        elif replies == 'D' or replies == 'd':
            return redirect(phaseD)
        elif replies == 'E' or replies == 'e':
            return redirect(phaseE)
        else:
            error = "Please enter Correct Input!"
        return render(request, 'index.html',{'replies':replies,'error':error}) 
    else:
        return redirect('login')

def getdata(url): 
    r = requests.get(url) 
    return r.text

def phaseB(request):
    if request.user.is_authenticated:
        replies = request.session['first_reply']
        htmldata = getdata("https://covid-19tracker.milkeninstitute.org/") 
        soup = BeautifulSoup(htmldata, 'html.parser') 
        result = str(soup.find_all("div", class_="is_h5-2 is_developer w-richtext"))
        res = [result[46:86],result[139:226],result[279:305],result[358:375]]
        return render(request, 'phaseB.html',{'res':res,'replies':replies})
    else:
        return redirect('login')

def phaseA(request):
    if request.user.is_authenticated:
        ic = []
        replies = request.session['first_reply']
        replya = request.POST.get('replya')
        request.session['second_reply'] = replya
        if replya == '1':
            c1=states.getdata('Total')
            c2=c1.keys()
            c3=c1.values()
            c2=list(c2)
            c3=list(c3)
            c2.remove('Total')
            c3.pop(0)
            for i in zip(c2,c3):
                ic.append(i)
        elif replya == '2':
            return redirect('phaseA2')
        return render(request, 'phaseA.html',{'ic':ic,'replya':replya,'replies':replies})
    else:
        return redirect('login')

def phaseA2(request):
    if request.user.is_authenticated:
        sc = []
        replies = request.session['first_reply']
        replya = request.session['second_reply']
        state = request.POST.get('states')
        if state is not None:
            v1=states.getdata(state)
            v2=v1.keys()
            v3=v1.values()
            v2=list(v2)
            v3=list(v3)
            v2.remove('Total')
            v3.pop(0)
            for i in zip(v2,v3):
                sc.append(i)
        return render(request, 'phaseA2.html',{'sc':sc,'state':state,'replies':replies,'replya':replya})
    else:
        return redirect('login')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email)
                user.save();
                messages.info(request,'User Created')
                return redirect('login')
        else:
            messages.info(request,'Password not matched')
            return redirect('register')
    else:
        return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')

    else:
        return render(request,'login.html')

def phaseC(request):
    if request.user.is_authenticated:
        replies = request.session['first_reply']
        replyc = request.POST.get('replyc')
        return render(request, 'phaseC.html',{'replyc':replyc,'replies':replies})
    else:
        return redirect('login')

def phaseD(request):
    if request.user.is_authenticated:
        replies = request.session['first_reply']
        replyd = request.POST.get('replyd')
        return render(request,'phaseD.html',{'replyd':replyd,'replies':replies})
    else:
        return redirect('login')

def phaseE(request):
    if request.user.is_authenticated:
        replies = request.session['first_reply']
        url = "https://www.worldometers.info/coronavirus/"
        ans = COVIDworld(url)
        case = []
        for i, j in ans.items():
            case.append(j)
        case1 = case[0]
        case2 = case[1]
        case3 = case[2]
        return render(request, 'phaseE.html',{'case1':case1,'case2':case2,'case3':case3,'replies':replies})
    else:
        return redirect('login')

def COVIDworld(url):
    data = requests.get(url) 
    soup = BS(data.text, 'html.parser') 
    total = soup.find("div", class_ = "maincounter-number").text 
    total = total[1 : len(total) - 2] 
    other = soup.find_all("span", class_ = "number-table") 
    recovered = other[2].text 
    deaths = other[3].text 
    deaths = deaths[1:] 
    ans ={'Total Cases' : total, 'Recovered Cases' : recovered,'Total Deaths' : deaths} 
    return ans
