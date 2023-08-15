from django.db import models

# Create your models here.
class Assessment(models.Model):
    company_name = models.CharField(max_length=50)
    product_name = models.CharField(max_length=50)
    contract_number = models.CharField(max_length=50)
    data_of_contract = models.DateField(auto_now=False, auto_now_add=False)
