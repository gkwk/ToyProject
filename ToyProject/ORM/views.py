from django.shortcuts import render, redirect

def index(request):
    return render(request,"ORM/index.html")
# Create your views here.
