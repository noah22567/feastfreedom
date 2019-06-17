from django.db import models
# from users.models import myUser
from django.contrib.auth.models import User

# Create your models here.


class ServiceProvider(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    # userID = models.ForeignKey(User,on_delete=models.CASCADE)
    userID = models.ManyToManyField(User)
    ServiceProviderName = models.CharField(('Service provider name'),max_length=20)


class Kitchen(models.Model):

    ServiceProviderID = models.ForeignKey(ServiceProvider,on_delete=models.CASCADE)
    Starttime = models.TimeField(('Start Time'),auto_now=False,blank=False)
    Endtime = models.TimeField(('End Time'),auto_now=False,blank=False)
    Kitchenimg = models.ImageField(upload_to="images/",blank=True)

    # def get_item(self):


