from django.db import models
from users.models import myUser
from django.contrib.auth.models import User
import os
from users.models import myUser
# Create your models here.


class ServiceProvider():
    id = models.ForeignKey(myUser,on_delete=models.CASCADE)
    ServiceProviderName = models.CharField(('Service provider name'),max_length=20)


class Kitchen(models.Model):

    userID = models.ForeignKey(myUser,on_delete=models.CASCADE)

    Starttime = models.TimeField(('Start Time'),auto_now=False,blank=False)
    Endtime = models.TimeField(('End Time'),auto_now=False,blank=False)
    # os.chdir('C:\\Users\\19198\\Desktop\\freastfreedom\\Feast-Freedom\\templates\\provider\\images')
    Kitchenimg = models.ImageField(upload_to="images",blank=True)

    # def get_item(self):



