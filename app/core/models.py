from django.db import models

# Create your models here.
class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)

    class Meta:
            abstract = True


class Spider(BaseModel):
    name = models.CharField(max_length=50, default='', blank=True)
    info = models.CharField(max_length=500, default='', blank=True)
    catch_url = models.CharField(max_length=1000, default='')
    header = models.CharField(max_length=2000, default='', blank=True)
    use_cookie = models.BooleanField(default=False)
    cookie = models.CharField(max_length=5000, default='', blank=True)
    data_type = models.CharField(default='html')
    re_format = models.TextField(default='', blank=True)
    script = models.TextField(default='', blank=True)
    type = models.IntegerField(default=1)
    thumb_up = models.IntegerField(default=0)
    # tags = models.ForeignKey()
    # belong = models.ForeignKey()


