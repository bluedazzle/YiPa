from django.contrib import admin
from app.YPMessage.models import Message, PersonalMessage, PrivateMessage
# Register your models here.

admin.site.register(Message)
admin.site.register(PersonalMessage)
admin.site.register(PrivateMessage)
