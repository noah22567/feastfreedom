from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import SignupProvider,KitchenCreate
from django.views.generic.edit import FormView


def registerProviderView(request):


    if request.method == 'POST':
        form = SignupProvider(request.POST)
        if form.is_valid():
            request.User.make_provider()
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignupProvider()
    return render(request, 'RegisterProvider.html', {form:'form'})

def registerKitchenView(request):

    template_name = 'RegisterProvider.html'
    form_class = KitchenCreate
    success_url = '/thanks/'

    # def form_valid(self, form):
    #     # This method is called when valid form data has been POSTed.
    #     # It should return an HttpResponse.
    #     form.send_email()
    #     return super().form_valid(form)

    print("Call kitchen create!!")
    if request.method == 'POST':
        form = KitchenCreate(request.POST)
        print(form)
        if form.is_valid():
            request.User.make_provider()
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        print("It is GET!!")
        form = KitchenCreate()
        # print("else states")
        print(type(form))
    #
    # print("test3")
    # print(form)
    return render(request, 'registertest.html', {form:'form'})




#     creation form
    # form --> UserID = request.User.pk







##########################################################################################
#                                                                                        #
#        add the checkp to the userclass and finish the fucking view before you test     #
#                                                                                        #
##########################################################################################