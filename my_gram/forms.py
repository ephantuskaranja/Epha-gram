from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
   class Meta:
       model = Profile
       exclude = ['user']

class UploadPicForm(forms.ModelForm):
   class Meta:
       model= Pictures
       exclude = ['user']
