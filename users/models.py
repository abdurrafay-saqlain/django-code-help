from django.db import models
from django.contrib.auth.models import AbstractBaseUser , AbstractUser,BaseUserManager # you need to identify which ABstractUser model will be use and why?
from django_countries.fields import CountryField
from .managers import *
from django.utils import timezone
from cities.models import BaseCountry

# Create your 
# models here.
class User(AbstractBaseUser,BaseCountry):
    username=None
    first_name=models.CharField(max_length=250,null=False)
    last_name=models.CharField(max_length=250,null=False)
    profile_picture=models.ImageField(upload_to='images/',null=False)
    email=models.EmailField(max_length=250,null=False,unique=True)
    education=models.CharField(max_length=250,null=True)
    country=CountryField(null=False)
    language=models.CharField(max_length=250,null=False)
    address=models.CharField(max_length=250,null=False)
    city = models.TextField()
    postal_code=models.IntegerField()
    
    class Meta(BaseCountry.Meta):
            pass
    objects=UserManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS = []
    USER_TYPE_CHOICES = (
        ('admin', 'ADMIN'),
        ('freelancer', 'FREELANCER'),
        ('client', 'CLIENT'),
    )
    user_type = models.CharField(max_length=250,choices=USER_TYPE_CHOICES, null=False, default='admin')
    is_client_profile=models.BooleanField(default=False)
    is_freelancer_profile=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=True)
    
    def has_perm(self,perm,obj=None):
        return True
    def has_module_perms(self,app_label):
        return True
  
    class Meta:
         db_table='users'
class Portfolio(models.Model):  
    title=models.CharField(max_length=250,null=False)
    description=models.TextField(max_length=250,null=False)
    
    class Meta:
        db_table='portfolio'
    
class Skills(models.Model):
    name=models.CharField(max_length=250,null=False)
    description=models.TextField(max_length=250,null=False)
    
    class Meta:
        db_table='skills'


class Education(models.Model):
       
    degree=models.CharField(max_length=250, null=False)
    high_level=models.CharField(max_length=250, null=False)
    secondary_level=models.CharField(max_length=250,null=False)
    
    class Meta:
        db_table='education'
 
class Certification(models.Model):
    title=models.CharField(max_length=250,null=False)
    description=models.CharField(max_length=250,null=True)
    
    class Meta:
        db_table = 'certification'
    
    
    
    
class Freelancer(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='freelance_profile', null=True)
    age=models.IntegerField()
    country = CountryField(null=False) 
    skills=models.ForeignKey(Skills,on_delete=models.CASCADE,related_name='freelance_profile',null=False)
    certification=models.ForeignKey(Certification,on_delete=models.CASCADE,related_name='education',null=True)
    portfolio=models.ForeignKey(Portfolio,on_delete=models.CASCADE,related_name='portfolio',null=False)
    linkedin_url=models.URLField(null=True)
    facebook_url=models.URLField(null=True)
    behance_url=models.URLField(null=True)
    
    class Meta:
        db_table = 'freelancer'
    
class Client(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_profile', null=False)
      description=models.TextField(null=False)
      card_number=models.IntegerField()
      expiration_month=models.IntegerField()     
      expiration_year=models.IntegerField()     
      security_code=models.IntegerField()
    
     
      class Meta:
            db_table = 'client'
      
    
