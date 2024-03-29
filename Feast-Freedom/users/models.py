from django.db import models
from django.contrib.auth.models import User,AbstractUser,PermissionsMixin,AbstractBaseUser
from mainset import settings

# Create your models here.
class myUser(AbstractBaseUser):


    is_superuser = False

    is_staff = False

    is_provider = models.BooleanField("provider", default=False)

    securityquestion1 = models.CharField(('Security question 1: What is the name of hospital were you born in?'),
                                         max_length=20,blank=False,null=False)
    securityquestion2 = models.CharField(('Security question 2: What was your childhood friends name?'),
                                         max_length=20,blank=False,null=False)
    def make_provider(self):
        self.is_provider = True

    # something = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

