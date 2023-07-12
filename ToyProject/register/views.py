from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.http import JsonResponse
from django.middleware.csrf import get_token

from .forms import UserForm, LoginForm

# def register(request):
#     return render(request,"register/register.html")

def modal(request):
    return render(request,"register/modal.html")



def register(request):
    if request.user.is_authenticated: # 유저가 로그인한 상태인지 확인한다.
        # 홈으로 보낸다.
        return redirect('/')
    else:
        try:        
            if request.method == "POST":
                # POST 정보로 UserForm 생성
                register_form = UserForm(request.POST)
                
                # 유효성검사
                if register_form.is_valid():
                    register_form_cleand = UserForm({"username" : register_form.cleaned_data["username"],
                                                    "email" : register_form.cleaned_data["username"],
                                                    "password1" : register_form.cleaned_data["password1"],
                                                    "password2" : register_form.cleaned_data["password2"],
                                                    "last_name" : register_form.cleaned_data["username"].split("@")[0],
                                                    })
                    
                    if register_form_cleand.is_valid():
                        register_form_cleand.save()
                        return redirect('/')
            else:
                register_form = UserForm()
                
        except:
            pass
        
        
        return render(request, 'register/register.html', {'form': register_form})