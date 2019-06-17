from django.db import models
from django.contrib.auth.models import User,AbstractUser,PermissionsMixin,AbstractBaseUser

# Create your models here.
# class myUser(User):
#
#
#     is_superuser = False
#     is_staff = False
#     # username = models.CharField(blank=True)
#     # first_name = models.CharField(('first name'), max_length=30, blank=True, unique=True)
#     is_provider = models.BooleanField("provider", default=False)
#     securityquestion1 = models.CharField(('Security question 1: What is the name of hospital were you born in?'),
#                                          max_length=20,blank=False)
#     securityquestion2 = models.CharField(('Securtiy question 2: What was your childhood friends name?'),
#                                          max_length=20,blank=False)
