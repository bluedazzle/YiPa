#coding:utf-8

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from app.core.models import BaseModel


import app.future
# Create your models here.


class Custmor(BaseModel, AbstractBaseUser):
    gender_choice = [(0, '请选择'),
                     (1, '公蜘蛛'),
                     (2, '母蜘蛛'),
                     (3, '保密')]

    email = models.CharField(max_length=50, unique=True)
    nick = models.CharField(max_length=50, default='', blank=True)
    birthday = models.DateTimeField(default=None)
    gender = models.IntegerField(default=0, choices=gender_choice)

    level = models.IntegerField(default=1)
    exp = models.IntegerField(default=0)
    coin = models.IntegerField(default=0)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = 'email'

    def __unicode__(self):
        return self.email


