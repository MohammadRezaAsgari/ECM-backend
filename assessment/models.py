from django.db import models
import os


def path_and_rename(instance, filename):
    upload_to = 'uploads/'
    filename = str()
    try:
        filename = '{}'.format(instance.contract_number)
    except:
        filename = 'defualt'
        
    return os.path.join(upload_to, filename)



class Assessment(models.Model):
    company_name = models.CharField(max_length=50)
    product_name = models.CharField(max_length=50)
    contract_number = models.CharField(max_length=50, unique=True)
    date_of_contract = models.CharField(max_length=50)
    contract_photo = models.ImageField(upload_to=path_and_rename, null=True)
    
    class Meta:
       unique_together = ("company_name", "product_name")
