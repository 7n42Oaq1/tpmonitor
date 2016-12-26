from __future__ import unicode_literals


from django.db import models

# Create your models here.
class device(models.Model):
    sn = models.CharField(max_length=15)
    name = models.CharField(max_length=15)
    temperature = models.FloatField()
    alarmTpMin = models.FloatField(blank=True,null=True)
    alarmTpMax = models.FloatField(blank=True,null=True)
    updatetime = models.DateTimeField('status update')
    status = models.BooleanField(default='true')

    def __str__(self):
        return self.name

    @staticmethod
    def getdevice(name):
        return device.objects.get(name=name)