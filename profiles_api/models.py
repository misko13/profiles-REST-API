from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Managre User Profiles"""
    
    def create_user(self, email, name, password=None ):
        """Create a standard user"""
        if not email:
            raise ValueError('user must have email address')
        
        email=self.normalize_email(email)
        user=self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password ):
        """Create a superuser"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for userrs in the system.  Extend model.object overide length.  
        Our model: Here we will extend the standard Django Class we have imported. We will overide user bame to use email"""
    email = models.EmailField(max_length=255, unique=True)
    name  = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff  = models.BooleanField(default=False)

    object = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrive full name of user - we use email actually"""
        return self.name
    
    def get_short_name(self):
        """Retrive short name of user"""
        return self.name
    
    def __str__(self):
        """Return - convert to string - rappresentation of user"""
        return self.email