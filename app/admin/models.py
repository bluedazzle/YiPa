from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from app.core.models import BaseModel
# Create your models here.


class Admin(AbstractBaseUser, BaseModel):
    username = models.CharField(max_length=50, unique=True)
    nick = models.CharField(max_length=50)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = 'username'

    def __unicode__(self):
        return self.username


