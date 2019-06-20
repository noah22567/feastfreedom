from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import ServiceProvider,Kitchen
from django.forms import ModelForm
from users.models import myUser

class SignupProvider(UserCreationForm):

    ServiceProviderName = forms.CharField(max_length=30, required=True)

    userID = forms.ModelChoiceField(queryset=myUser.objects.all(),
            widget=forms.HiddenInput())



    class Meta:
        model = ServiceProvider
        fields = ("ServiceProviderName",'userID',
                  )




class KitchenCreate(forms.ModelForm):

    # Starttime = forms.CharField(max_length=30, required=True)
    # Endtime = forms.CharField(max_length=30, required=True)
    # Kitchenimg = forms.CharField(max_length=30, required=True)

    userID = forms.ModelChoiceField(queryset=myUser.objects.all(),
            widget=forms.HiddenInput())

    class Meta:
        model = Kitchen
        fields = ["Starttime","Endtime","Kitchenimg",'userID'] #"UserID"
        # fields = ["Starttime","Endtime","Kitchenimg",]



