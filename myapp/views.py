from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponseRedirect
from myapp.forms import EmpForm
from .models import Emp

def projectlist(request):
    projectlist=Emp.objects.all()
    return render(request,'projectlist.html', {'projectlist':projectlist})


def index(request):
    submitted=False
    stu = EmpForm()
    if request.method == "POST":
        form=EmpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/index?submitted=True')
    else:

        if 'submitted' in request.GET:
            submitted=True

    return render(request, "index.html", {'form': stu, 'submitted':submitted})


def createandviewbutton(request):
    return render(request,"createandviewbutton.html")

def bootstrap(request):
    return render(request,"bootstrap practice.html")

import datetime
# Create your views here.
# def index(request):
#     now = datetime.datetime.now()
#     html = "<html><body><h3>Now time is %s.</h3></body></html>" % now
#     return HttpResponse(html)    # rendering the template in HttpResponse


# Create your views here.
