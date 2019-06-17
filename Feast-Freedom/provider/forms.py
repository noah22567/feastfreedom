from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import ServiceProvider,Kitchen
from django.forms import ModelForm

class SignupProvider(forms.ModelForm):

    ServiceProviderName = forms.CharField(max_length=30, required=True)

    class Meta:
        model = ServiceProvider
        fields = ["ServiceProviderName","userID",]


class KitchenCreate(forms.ModelForm):

    # Starttime = forms.TimeField()
    # Endtime = forms.CharField()
    # Kitchenimg = forms.ImageField()

    class Meta:
        model = Kitchen
        # fields = ["ServiceProviderID","Starttime","Endtime","Kitchenimg",]
        fields = ["Starttime","Endtime","Kitchenimg",]



