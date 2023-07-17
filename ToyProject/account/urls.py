from django.urls import path, include,reverse_lazy
from django.contrib.auth import views as auth_views

import account.views
import account.forms

urlpatterns = [
    path("login/",account.views.login_view,name="login"),
    path("logout/",account.views.logout_view,name="logout"),
    path("register/",account.views.register_view,name="register"),
    path("register_complete/",account.views.register_complete_view,name="register_complete"),
    
    path('password_reset/', account.views.UserPasswordResetView.as_view(template_name='account/password_reset/password_reset_form.html',form_class=account.forms.UserPasswordResetForm,email_template_name="account/password_reset/password_reset_email.html"),name="password_reset"),
    path('password_reset_done/', account.views.RefererCheck_PasswordResetDoneView, name="password_reset_done"),    
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset/password_reset_confirm.html',form_class=account.forms.UserSetPasswordForm,success_url = reverse_lazy("account:password_reset_complete")),name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset/password_reset_complete.html'), name="password_reset_complete"),

]
