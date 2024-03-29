from django import forms
from django.contrib.auth.models import User
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class UserUpdate(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']


class ProfileUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']