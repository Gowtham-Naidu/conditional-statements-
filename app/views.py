from django.shortcuts import render

# Create your views here.

def cond(request):
    d={
        'a':1000,
        'b':2000,
        'c':500
    }
    return render(request,'app.html',d)