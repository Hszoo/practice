from django.shortcuts import render

# Create your views here.

def saveshome(request) :
    return render(request, "index.html")