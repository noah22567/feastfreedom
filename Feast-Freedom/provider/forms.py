from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import ServiceProvider,Kitchen
from django.forms import ModelForm

class SignupProvider(UserCreationForm):

    ServiceProviderName = forms.CharField(max_length=30, required=True)


    email = forms.EmailField(max_length=254, help_text='Required. Confirm Email Address.')

    securityquestion1 = forms.CharField(max_length=50, required=False, help_text='Optional.')

    securityquestion2 = forms.CharField(max_length=50, required=False, help_text='Optional.')

    class Meta:
        model = ServiceProvider
        fields = ("ServiceProviderName",'username', 'email','securityquestion1',
                  'securityquestion2','password1', 'password2',
                  )



class KitchenCreate(forms.ModelForm):

    # Starttime = forms.CharField(max_length=30, required=True)
    # Endtime = forms.CharField(max_length=30, required=True)
    # Kitchenimg = forms.CharField(max_length=30, required=True)

    class Meta:
        model = Kitchen
        fields = ["Starttime","Endtime","Kitchenimg",] #"UserID"
        # fields = ["Starttime","Endtime","Kitchenimg",]



