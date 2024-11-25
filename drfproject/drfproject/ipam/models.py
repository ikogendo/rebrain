from django.db import models

# Create your models here.


class station(models.Model):
    name = models.CharField(max_length=64)
    user = models.CharField(max_length=64)
    date_startuse = models.DateTimeField(auto_now=False)
    date_lastuse = models.DateTimeField(auto_now=False)
    ip_address = models.GenericIPAddressField(default='192.168.0.1')
    type_address = models.CharField(max_length=6,default='DHCP')
    place = models.ForeignKey('Build',on_delete=models.PROTECT,null=True)
    
    
    
    def __str__(self):
        return self.name
    
    
class Build(models.Model):
    code = models.CharField(default='CY-',max_length=10)
    city = models.CharField(max_length=64)
    floor = models.IntegerField(default='0')
    street = models.CharField(max_length=128,default='Makariou')
    build_number = models.IntegerField()
    
    def __str__(self):
        return self.code
    