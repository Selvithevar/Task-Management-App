from django.contrib.auth.forms import UserCreationForm
# from .models import User
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput,TextInput



class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'})
        }

class CustomUserForm(UserCreationForm):
    # username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter username'}))
    # email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter email'}))
    # password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter password1'}))
    # password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm password2'}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class CreateTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['task','description','due_date',]
        exclude = ['user',]
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'})
        }

