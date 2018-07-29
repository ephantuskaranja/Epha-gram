from django import forms
from .models import Profile, Pictures, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
   class Meta:
       model = Profile
       exclude = ['user']

class UploadPicForm(forms.ModelForm):
   class Meta:
       model= Pictures
       exclude = ['user']


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user','picture']
