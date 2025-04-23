from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

class CustomLogin(AuthenticationForm):
    username = forms.CharField(
        widget= forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'enter your username' 
        })
    )

    password = forms.CharField(
        label= 'Password',
        widget= forms.PasswordInput(attrs={
            'class':'form-control',
            'placeholder':'enter your Password' 
        })
    )

class CustomRegister(UserCreationForm):
    username = forms.CharField(
        widget= forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'enter your username' 
        })
    )
        
    password1 = forms.CharField(
        label= 'Password',
        widget= forms.PasswordInput(attrs={
            'class':'form-control',
            'placeholder':'enter your Password' 
        })
    )

    password2 = forms.CharField(
        label= 'Conform Password',
        widget= forms.PasswordInput(attrs={
            'class':'form-control',
            'placeholder':'Confirm Password' 
        })
    )
    class Meta:
        model = User
        fields = ('username','password1','password2')