from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import SignupProvider,KitchenCreate
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Kitchen
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def registerProviderView(request):

    if request.method == 'POST':
        initial = {'ServiceProviderName': request.session.get('ServiceProviderName', None)}
        form = SignupProvider(request.POST,initial=initial)
        if form.is_valid():
            request.session['ServiceProviderName'] = form.cleaned_data['ServiceProviderName']
            return HttpResponseRedirect(reverse('registerKitchenView'))
    else:
        form = SignupProvider()
    return render(request, 'RegisterProvider.html', {'form':form})


def registerKitchenView(request):

    if request.method == 'POST':
        form = KitchenCreate(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = KitchenCreate()
    return render(request, 'RegisterKitchen.html', {'form':form})


class viewKitchen(DetailView):
    # lookup_field = pk
    model = Kitchen


class listViewKitchen(ListView):
    model = Kitchen
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()

        return context




from django.http import HttpResponse
import os
def my_image(request):

    lookup_field = Kitchenimg

    # os.chdir('C:\\Users\\19198\\Desktop\\freastfreedom\\Feast-Freedom\\templates\\provider\\images')


    image_data = open(lookup_field, "rb").read()

    return HttpResponse(image_data, mimetype="image/png")









##########################################################################################
#                                                                                        #
#        add the checkp to the userclass and finish the fucking view before you test     #
#                                                                                        #
##########################################################################################