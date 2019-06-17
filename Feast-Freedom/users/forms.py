from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUpForm(UserCreationForm):

    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')

    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')

    email = forms.EmailField(max_length=254, help_text='Required. Confirm Email Address.')

    class Meta:
        model = User
        fields = ('username', 'email','first_name', 'last_name','securityquestion1',
                  'securityquestion2','password1', 'password2',
                  )

# class SignupProvider():
