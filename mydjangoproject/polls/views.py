from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Feature,Friends,Friend
from django.contrib.auth.models import User, auth
from django.contrib import messages
def index(request):
    features = Friend.objects.all()
    return render(request,'index.html',{'features':features})
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Exists')
                return redirect('/register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'User Already Exists')
                return redirect('/register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save();
                return redirect('/')
        else:
            messages.info(request,'Password Not The Same')
            return redirect('/register')
    else:
        return render(request,'register.html')
def counter(request):
    words = request.POST['text']
    count = len(words.split())
    return render(request,'counter.html',{'count':count})
def splitting(request):
    text = request.POST['split']
    splitted = text.split()
    return render(request,'splitting.html',{'splitted':splitted})
def removepunc(request):
    punct = request.POST['punctuation']
    # puncts = punct
    punctuated = '''", '/;[]{}()!?:-&%$#*@"'''
    analyze =""
    for char in punct:
        if char not in punctuated:
            analyze = analyze + char
    return render(request,'removepunc.html',{'punctuations':analyze})




def contact(request):
    return HttpResponse('This is contact page')
