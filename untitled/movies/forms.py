from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#from phonenumber_field.modelfields import PhoneNumberField



class TrueUser(UserCreationForm):

    email = forms.EmailField()
    #phone = PhoneNumberField(null=False, blank=False, unique=True)

    class Meta():
        model = User
        fields = ['username',' email',  'password', 'password1']



