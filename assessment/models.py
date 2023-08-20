from django.db import models
import os


# def path_and_rename(instance, filename):
#     upload_to = 'uploads/'
#     filename = str()
#     filename = 'assessment{}'.format(instance.assessment.id)
#     return os.path.join(upload_to, filename)



class AssessmentPhoto(models.Model):
    photo = models.ImageField(upload_to='uploads/',null=True , blank=True)


class Assessment(models.Model):
    company_name = models.CharField(max_length=50)
    product_name = models.CharField(max_length=50)
    contract_number = models.CharField(max_length=50, unique=True)
    date_of_contract = models.CharField(max_length=50)
    contract_photo = models.ForeignKey(AssessmentPhoto, on_delete=models.SET_NULL, null=True , blank=True)
     
    class Meta:
       unique_together = ("company_name", "product_name")

