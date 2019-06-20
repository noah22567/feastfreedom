from django.forms import ModelForm
from .models import MenuItem




class createMenuItem(ModelForm):

    class Meta:
        model = MenuItem
        fields = ("name", "price", "is_veg", "kitchen", )

    # def __init__(self, *args, **kwargs):
    #     super(ModelForm, self).__init__(*args, **kwargs)
    #

