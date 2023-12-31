from django.db import models
from django.contrib.auth.models import User
from .constants import GENDER_TYPE
# Create your models here.


# django amaderke build in user make korar facility
#(USER, backentd)
class UserAccount(models.Model):
    
    user=models.OneToOneField(User,related_name='account',on_delete=models.CASCADE)
    account_no=models.IntegerField(unique=True) # account no 2 jon userer same hote parbe na 
    birth_date=models.DateField(null=True,blank=True)
    gender=models.CharField(max_length=10,choices=GENDER_TYPE)
    def __str__(self):
        return f'Account no: {self.account_no}'
    
    
class UserAddress(models.Model):
    user=models.OneToOneField(User,related_name='address',on_delete=models.CASCADE)
    street_address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    postal_code=models.IntegerField()
    country=models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.user.email) # uporer function ei function same kaj korbe
    
    