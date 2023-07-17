from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404,JsonResponse
from django.contrib.auth import views as auth_views
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import User
from django.middleware.csrf import get_token
# from django.contrib.auth.models import *
from django.contrib.auth import authenticate, login, logout

from account.forms import UserForm, LoginForm




def login_view(request):
    try:
        if request.user.is_authenticated: # 유저가 로그인한 상태인지 확인한다.
            # 로그인한 상태에서 로그인 페이지에 강제 접속한다면 홈으로 보낸다.
            return redirect('/')
        else:
            if request.method == 'POST':
                login_form = LoginForm(request.POST)
                
                if login_form.is_valid():                
                    user_username = login_form.cleaned_data["username"]
                    user_password = login_form.cleaned_data["password"]
                    user_remember_me = login_form.cleaned_data["remember_me"]
                    
                    user = authenticate(username=user_username, password=user_password)

                    if not user is None:
                        login(request,user)
                        
                        if user_remember_me:
                            # 30일간 세션이 유지된다. (3600sec * 24 * 30)
                            request.session.set_expiry(3600*24*30)
                        else:
                            request.session.set_expiry(0)
                        
                        return JsonResponse({'status': 'success'})

            return JsonResponse({'status': 'error', 'csrf_token': get_token(request)})
    except:
        pass
        
    return redirect('/')

def logout_view(request):
    try:
        # 유저가 로그인한 상태인지 확인한다.
        if request.user.is_authenticated: 
            logout(request)
            # 로그아웃한다.
            return redirect('/')
    except:
        pass
    
    return redirect('/')


def register_view(request):
    try:
        if request.user.is_authenticated: # 유저가 로그인한 상태인지 확인한다.
            # 홈으로 보낸다.
            return redirect('/')
        else:
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
                        return redirect('account:register_complete')
            else:
                register_form = UserForm()
    except:
        register_form = UserForm()
        
    
    return render(request, 'account/register.html', {'form': register_form})


def register_complete_view(request):
    # referer참조로 직접 접근을 최대한 차단
    return render(request, 'account/register_complete.html')



class UserPasswordResetView(auth_views.PasswordResetView):
    success_url = reverse_lazy("account:password_reset_done")
    
    def form_valid(self, form):
        if User.objects.filter(email=self.request.POST.get("email")).exists():
            return super().form_valid(form)
        else:
            return render(self.request,'account/password_reset/password_reset_form.html',context={"form" : form, "error" : True})

def RefererCheck_PasswordResetDoneView(request):
    domain = str(get_current_site(request))
    # 127.0.0.1:8000    
    Received_referer = request.META.get('HTTP_REFERER', '').split("/")[1:]
    Received_referer = [i for i in Received_referer if i != ""]
    target_referer = "password_reset"
    
    if Received_referer == [domain,"account",target_referer]:
        return auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset/password_reset_done.html')(request)
    else:
        return redirect("index")








# def login_view(request):
#     # return HttpResponse("login")
#     if request.method == 'POST':
#             login_form = LoginForm(request.POST)
            
#             if login_form.is_valid():                
#                 user_username = login_form.cleaned_data["username"]
#                 user_password = login_form.cleaned_data["password"]
#                 user_remember_me = login_form.cleaned_data["remember_me"]
                
#                 user = authenticate(username=user_username, password=user_password)
    
    
    
#     return JsonResponse({"status": "error","csrf_token" : get_token(request)})

# def logout_view(request):
#     return HttpResponse("logout")


# def modal(request):
#     return render(request,"register/modal.html")



