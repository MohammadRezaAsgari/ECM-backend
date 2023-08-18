from django.db import models
from django_jalali.db import models as jmodels

# Create your models here.
class Assessment(models.Model):
    company_name = models.CharField(max_length=50)
    product_name = models.CharField(max_length=50)
    contract_number = models.CharField(max_length=50, unique=True)
    date_of_contract = models.DateField()
    
    class Meta:
       unique_together = ("company_name", "product_name")
