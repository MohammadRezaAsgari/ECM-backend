from django.db import models
from django.dispatch import receiver
import os


class Contract(models.Model):
    company_name = models.CharField(max_length=50)
    product_name = models.CharField(max_length=50)
    contract_number = models.CharField(max_length=50, unique=True)
    date_of_contract = models.CharField(max_length=50)

    contract_total_price = models.CharField(max_length=50, null=True, blank=True)
    contract_deadline_date = models.CharField(max_length=50, null=True, blank=True)
    approved_discount = models.CharField(max_length=50, null=True, blank=True)
    certificate_renewal = models.BooleanField(null=True,blank=True)
    certificate_renewal_description = models.TextField(max_length=500, null=True, blank=True)
    landline_phone_number = models.CharField(max_length=50, null=True, blank=True)
    interface_name = models.CharField(max_length=50, null=True, blank=True)
    postal_code = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)

    first_phase_deposit_date = models.CharField(max_length=50, null=True, blank=True)
    first_phase_price = models.CharField(max_length=50, null=True, blank=True)
    first_phase_deadline_date = models.CharField(max_length=50, null=True, blank=True)

    second_phase_deposit_date = models.CharField(max_length=50, null=True, blank=True)
    second_phase_price = models.CharField(max_length=50, null=True, blank=True)
    second_phase_deadline_date = models.CharField(max_length=50, null=True, blank=True)

    supplement_price = models.CharField(max_length=50, null=True, blank=True)
    supplement_date = models.CharField(max_length=50, null=True, blank=True)
     
    class Meta:
       unique_together = ("company_name", "product_name")


class PhaseOneDocument(models.Model):
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE)
    documents = models.FileField(upload_to='uploads/first_phase_documents/')


class PhaseTwoDocument(models.Model):
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE)
    documents = models.FileField(upload_to='uploads/second_phase_documents/')


class SupplementDocument(models.Model):
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE)
    receipt_photo = models.ImageField(upload_to='uploads/supplement_receipt_photo/')


class ContractPhoto(models.Model):
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='uploads/contracts_first_page_photo/')
    


#some handlers for removing photo file for model ContractPhoto
@receiver(models.signals.post_delete, sender=ContractPhoto)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.photo:
        if os.path.isfile(instance.photo.path):
            os.remove(instance.photo.path)

@receiver(models.signals.pre_save, sender=ContractPhoto)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_file = ContractPhoto.objects.get(pk=instance.pk).photo
    except ContractPhoto.DoesNotExist:
        return False

    new_file = instance.photo
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)


#some handlers for removing receipt_photo file for model PhaseOneDocument
@receiver(models.signals.post_delete, sender=PhaseOneDocument)
def auto_delete_file_on_delete1(sender, instance, **kwargs):
    if instance.documents:
        if os.path.isfile(instance.documents.path):
            os.remove(instance.documents.path)

@receiver(models.signals.pre_save, sender=PhaseOneDocument)
def auto_delete_file_on_change1(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_file = PhaseOneDocument.objects.get(pk=instance.pk).documents
    except PhaseOneDocument.DoesNotExist:
        return False

    new_file = instance.documents
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)



#some handlers for removing receipt_photo file for model PhaseTwoDocument
@receiver(models.signals.post_delete, sender=PhaseTwoDocument)
def auto_delete_file_on_delete3(sender, instance, **kwargs):
    if instance.documents:
        if os.path.isfile(instance.documents.path):
            os.remove(instance.documents.path)

@receiver(models.signals.pre_save, sender=PhaseTwoDocument)
def auto_delete_file_on_change3(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_file = PhaseTwoDocument.objects.get(pk=instance.pk).documents
    except PhaseTwoDocument.DoesNotExist:
        return False

    new_file = instance.documents
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)



#some handlers for removing receipt_photo file for model SupplementDocument
@receiver(models.signals.post_delete, sender=SupplementDocument)
def auto_delete_file_on_delete6(sender, instance, **kwargs):
    if instance.receipt_photo:
        if os.path.isfile(instance.receipt_photo.path):
            os.remove(instance.receipt_photo.path)

@receiver(models.signals.pre_save, sender=SupplementDocument)
def auto_delete_file_on_change6(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_file = SupplementDocument.objects.get(pk=instance.pk).receipt_photo
    except SupplementDocument.DoesNotExist:
        return False

    new_file = instance.receipt_photo
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)

