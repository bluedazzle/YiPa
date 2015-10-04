from django.db import models
from app.core.models import BaseModel
from app.custmor.models import Custmor
# Create your models here.

class Message(BaseModel):
    content = models.TextField(default='')
    read = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode(self.id)


class PersonalMessage(models.Model):
    message = models.OneToOneField(Message, related_name='mes_personal')
    belong = models.ForeignKey(Custmor)

    def __unicode__(self):
        return self.belong.email


class AllMessage(models.Model):
    message = models.OneToOneField(Message, related_name='mes_all')

    def __unicode__(self):
        return unicode(self.id)


class PrivateMessage(models.Model):
    message = models.OneToOneField(Message, related_name='mes_private')
    to = models.ForeignKey(Custmor, related_name='cus_to_mes', null=True, blank=True, on_delete=models.SET_NULL)
    m_from = models.ForeignKey(Custmor, related_name='cus_from_mes', null=True, blank=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return '%s to %s' % (self.m_from.email, self.to.email)


