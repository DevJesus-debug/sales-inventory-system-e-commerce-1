from .models import Profile
from django import forms
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User=get_user_model()
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('username', 'first_name', 'last_name', 'email')



class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('address','city','state', 'phone_no')
