from django.db import models
from django.utils import timezone
import json
# https://yildiz.dev/2017/09/12/how-to-use-scrapy-with-django-application/
class Property(models.Model):
    data = models.FloatField(null=True,blank=True) # this stands for our crawled data
    date = models.DateTimeField(default=timezone.now,null=True,blank=True)
    currency = models.CharField(max_length=100, null=True,blank=True)
    # This is for basic and custom serialisation to return it to client as a JSON.
    @property
    def to_dict(self):
        data = {
            'data': json.loads(self.data),
            'date': self.date
        }
        return data

    def __str__(self):
        return str(self.data)
    # code = models.CharField(unique=True, max_length=255, null=True)
    # price = models.CharField(max_length=255, null=True)
    # location = models.CharField(max_length=255, null=True)
    # district = models.CharField(max_length=255, null=True)
    # category = models.CharField(max_length=255, null=True)
    # status = models.CharField(max_length=255, null=True)
    # bedrooms = models.CharField(max_length=255, null=True)
    # bathrooms = models.CharField(max_length=255, null=True)
    # agent = models.CharField(max_length=255)
    # agent_contact = PhoneField(blank=True, help_text='Contact phone number')
    # agent_email = models.EmailField(max_length = 255)
    # agent_company = models.CharField(max_length=255)
    # date = models.DateTimeField(default=timezone.now)
    # name = models.CharField(max_length=255, null=True)
    # fun_fact = models.CharField(max_length=255, null=True)
    # def __str__(self):
    #     return self.code
