from django.db import models
from django.contrib import admin

# Create your models here.
class Infomation_dars(models.Model):
    name = models.CharField(u'Name', max_length=50)
    eamil_address = models.CharField(u'Email', max_length=50)
    number = models.CharField(u'Number', max_length=50)
    message_content = models.TextField(u'MESSAGE')

    def __str__(self):
        return self.name

class Infomation_szqt(models.Model):
    name = models.CharField(u'Name', max_length=50)
    eamil_address = models.CharField(u'Email', max_length=50)
    number = models.CharField(u'Number', max_length=50)
    message_content = models.TextField(u'MESSAGE')

    def __str__(self):
        return self.name