from django.shortcuts import render

# Create your views here.

def menushome(request) :
    return render(request, "index.html")