from django.db import models

# Create your models here.
class bank(models.Model):
    #account,count,currency,name,email,opened_date
    #id = models.AutoField()
    opened_date = models.DateField()
    names_owners = models.CharField(max_length=64)
    email_owners = models.EmailField(max_length=128)
    count_money = models.DecimalField(max_digits=1000,decimal_places=2)
    currency_money = models.CharField(max_length=2)
    
    def __str__(self):
        return (f"ID: {self.id} is {self.names_owners}, have email:{self.email_owners}. {self.names_owners} have {self.count_money} by {self.currency_money}. Account was opened: {self.opened_date}" )