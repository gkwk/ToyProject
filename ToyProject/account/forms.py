from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.core.validators import EmailValidator,MinLengthValidator,MaxLengthValidator,RegexValidator,ProhibitNullCharactersValidator

from django.forms import ModelForm, TextInput, EmailInput, PasswordInput

#ref : www.khidi.or.kr/includes/password.jsp

username_MinLengthValidator = MinLengthValidator(4,"최소길이 4")
username_MaxLengthValidator = MaxLengthValidator(20,"최대길이 20")
username_RegexValidator = RegexValidator(f"[^a-zA-Z0-9]+",message="허용되지 않은 문자 포함됨",inverse_match=True) # RegexValidator는 re.search를 사용하여 일치하는 문자가 없으면 오류를 출력한다. inverse_match를 사용하면 일치하는 문자가 존재하면 오류를 출력한다.
username_ProhibitNullCharactersValidator = ProhibitNullCharactersValidator()

password_MinLengthValidator = MinLengthValidator(8,"최소길이 8")
password_MaxLengthValidator = MaxLengthValidator(64,"최대길이 64")
password_RegexValidator = RegexValidator(f"[^a-zA-Z0-9\~\․\!\@\#\$\%\^\&\*\(\)\_\-\+\=\[\]\[\]\|\\\;\:\‘\“\<\>\,\.\?\/]+",message="허용되지 않은 문자 포함됨",inverse_match=True)
password_ProhibitNullCharactersValidator = ProhibitNullCharactersValidator()

email_MinLengthValidator = MinLengthValidator(5,"최소길이 5")
email_MaxLengthValidator = MaxLengthValidator(128,"최대길이 128")
email_RegexValidator = RegexValidator(f"[^a-zA-Z0-9\@\.]+",message="허용되지 않은 문자 포함됨",inverse_match=True)
email_emailValidator = EmailValidator()
email_ProhibitNullCharactersValidator = ProhibitNullCharactersValidator()


class UserForm(UserCreationForm):
    username = forms.CharField(validators=[email_MinLengthValidator,email_MaxLengthValidator,email_emailValidator,email_ProhibitNullCharactersValidator],label="사용자 이름",error_messages={"required" : "필요"})
    
    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email", "last_name")
        
        
class LoginForm(forms.Form):
    username = forms.CharField(validators=[email_MinLengthValidator,email_MaxLengthValidator,email_emailValidator,email_ProhibitNullCharactersValidator],label="사용자 이름",error_messages={"required" : "필요"})
    password = forms.CharField(validators=[password_MinLengthValidator,password_MaxLengthValidator,password_RegexValidator,password_ProhibitNullCharactersValidator])
    remember_me = forms.BooleanField(required=False)
    
    # class Meta:
    #     fields = ("username", "password", "remember_me")
        
# class LoginForm(AuthenticationForm):
#     username = forms.CharField(validators=[email_MinLengthValidator,email_MaxLengthValidator,email_emailValidator,email_ProhibitNullCharactersValidator],label="사용자 이름",error_messages={"required" : "필요"},required=True)
#     password = forms.CharField(validators=[password_MinLengthValidator,password_MaxLengthValidator,password_RegexValidator,password_ProhibitNullCharactersValidator],required=True)

#     remember_me = forms.BooleanField(required=False)
    
#     class Meta:
#         fields = ("username", "password", "remember_me")