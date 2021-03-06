from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login ,logout,get_user_model
User=get_user_model()
from .models import Profile,Tests
from django_ace import AceWidget
class ProfileForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields=['admissionno','status']

class UserRegisterForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','password','email']


class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','password']
class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    def clean(self):
        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")
        user=authenticate(username=username,password=password)
        if not user:
            raise forms.ValidationError("THis user does not exist")
        if not user.check_password(password):
            raise forms.ValidationError("Incorrect Password")
        if not user.is_active:
            raise forms.ValidationError("This user is no longer active")
        return super(LoginForm,self).clean()
