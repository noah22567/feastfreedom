from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import myUser

class SignUpForm(UserCreationForm):

    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')

    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')

    email = forms.EmailField(max_length=254, help_text='Required. Confirm Email Address.')

    securityquestion1 = forms.CharField(max_length=50, required=False, help_text='Optional.')

    securityquestion2 = forms.CharField(max_length=50, required=False, help_text='Optional.')

    class Meta:
        model = myUser
        fields = ('username', 'email','first_name', 'last_name','securityquestion1',
                  'securityquestion2','password1', 'password2',
                  )

# class SignupProvider():
