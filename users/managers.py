from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser , AbstractUser,BaseUserManager
class UserManager(BaseUserManager):
     def create_user(self,email,password,**extra_fields):
  
        if not email:
            raise ValueError('The Email must be set')
        email=self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user

     def create_freelancer(self,email,password,**kwargs):
         kwargs.setdefault('user_type','freelancer')
         return self.create_user(email,password,**kwargs)
     
     def create_client(self, email, password, **kwargs):
            kwargs.setdefault('user_type', 'client')
            return self.create_user(email, password, **kwargs)

   
     
     def create_superuser(self,email,password,**kwargs):
         kwargs.setdefault('user_type','admin')
         return self.create_user(email,password,**kwargs)
     


    
    # Add other custom methods if needed

