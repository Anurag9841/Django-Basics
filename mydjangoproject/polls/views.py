from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def counter(request):
    words = request.GET['text']
    count = len(words.split())
    return render(request,'counter.html',{'count':count})
def splitting(request):
    text = request.GET['split']
    splitted = text.split()
    return render(request,'splitting.html',{'splitted':splitted})
def removepunc(request):
    punct = request.GET['punctuation']
    # puncts = punct
    punctuated = '''", '/;[]{}()!?:-&%$#*@"'''
    analyze =""
    for char in punct:
        if char not in punctuated:
            analyze = analyze + char
    return render(request,'removepunc.html',{'punctuations':analyze})


def about(request):
    return HttpResponse('''<h1>About_Page</h1><a href='https://docs.djangoproject.com/en/4.2/intro/tutorial02/'>About_Page</a>''')

def contact(request):
    return HttpResponse('This is contact page')
