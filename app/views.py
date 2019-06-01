from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    context = {}
    return render(request,'index.html', context)

def home(request):
    context = {}
    return render(request,'home.html', context)

def about(request):
    context = {}
    return render(request,'about.html', context)

#word_dict에 word가 있는지, word_dict[word]는 value, word는 key값
def result(request):
    text = request.GET['textarea']
    check = request.GET['search']
    checkvalue=0
    words = text.split()
    word_dict={}
    for word in words:
         if word in word_dict:
            word_dict[word]+=1
         else:
            word_dict[word]=1
    if check in word_dict:
        checkvalue=word_dict[word]
    context = {'total':text, 'split':words, 'num':len(words), 'dict':word_dict.items(),'find':checkvalue, 'searchval':check}
    return render(request,'result.html', context)



