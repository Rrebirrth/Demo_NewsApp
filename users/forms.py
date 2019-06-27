from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from .models import Profile



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=15, label='First name')
    last_name = forms.CharField(max_length=15, label='Last name')
    

    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name', 'password1','password2' ]



class UserUpdateFrom(forms.ModelForm):
    email = forms.EmailField(required=False)
    first_name = forms.CharField(max_length=15, label='First name',required=False)
    last_name = forms.CharField(max_length=15, label='Last name',required=False)
    
   
    def __init__(self, *args, **kwargs):
        super(UserUpdateFrom, self).__init__(*args, **kwargs)
        self.fields['username'].required = False


    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name']


        

class ProfileUpdateFrom(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileUpdateFrom, self).__init__(*args, **kwargs)
        self.fields['image'].required = False
    class Meta:
        model = Profile
        fields = ['image']















