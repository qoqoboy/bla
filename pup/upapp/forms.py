from django import forms
from django.contrib.auth.models import User
from .models import Userpi

class Userform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')

class Userpif(forms.ModelForm):
    class Meta():
        model = Userpi
        fields = ('portfoliosite','profilepic')
        
