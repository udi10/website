#i have created this file
from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return render(request, 'index.html')
    # return HttpResponse('''hello harry <a href="https://www.youtube.com/watch?v=zP2_X2oE5Ak">code with harry</a>''')

def about(request):
    return HttpResponse("about hello harry")

def removepunc(request):
    print(request.GET.get('text','default'))
    return HttpResponse("remove punc")

def capfirst(request):
    return HttpResponse("capitalize first")

def newlineremove(request):
    return HttpResponse("capitalize first")


def spaceremove(request):
    return HttpResponse("space remover")

def charcount(request):
    return HttpResponse("charcount ")