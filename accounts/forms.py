from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.contrib.auth.models import User



class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'age',) # new

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'age',) # new


class EditProfileForm(UserChangeForm):
    email=forms.EmailField(widget = forms.EmailInput)
    first_name=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_login=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_superuser=forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_staff=forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_active=forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    date_joined=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    age = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','username','email','age','password') # new