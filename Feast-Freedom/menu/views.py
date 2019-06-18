from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import MenuItem
from .forms import createMenuItem

class MenuList(ListView):
    model = MenuItem


class CreateMenuItem(request):
    if request.method == 'POST':
        form = createMenuItem(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = createMenuItem()
    return render(request, 'CreatMenuItem.html', {'form': form})


