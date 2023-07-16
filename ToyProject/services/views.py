from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404,JsonResponse
# Create your views here.

def train_view(request):
    return render(request,"services/train.html")

def predict_view(request):
    return render(request,"services/predict.html")
