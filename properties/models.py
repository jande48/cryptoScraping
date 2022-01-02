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

class YieldlyToAlgoRatio(models.Model):
    date = models.DateTimeField(default=timezone.now,null=True,blank=True)
    ratio = models.FloatField(null=True,blank=True) # this stands for our crawled data

