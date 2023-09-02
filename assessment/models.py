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


class PhaseOneFiles(models.Model):
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE)
    receipt_photo = models.ImageField(upload_to='uploads/first_phase_receipt_photo/')
    documents = models.FileField(upload_to='uploads/first_phase_final_documents/')


class PhaseTwoFiles(models.Model):
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE)
    receipt_photo = models.ImageField(upload_to='uploads/first_phase_receipt_photo/')
    functional_document = models.FileField(upload_to='uploads/second_phase_functional_documents/')
    vulnerability_document = models.FileField(upload_to='uploads/second_phase_vulnerability_documents/')


class SupplementFiles(models.Model):
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE)
    receipt_photo = models.ImageField(upload_to='uploads/supplement_receipt_photo/')


class ContractPhoto(models.Model):
    photo = models.ImageField(upload_to='uploads/contracts_first_page_photo/')
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE)



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


#some handlers for removing receipt_photo file for model PhaseOneFiles
@receiver(models.signals.post_delete, sender=PhaseOneFiles)
def auto_delete_file_on_delete1(sender, instance, **kwargs):
    if instance.receipt_photo:
        if os.path.isfile(instance.receipt_photo.path):
            os.remove(instance.receipt_photo.path)

@receiver(models.signals.pre_save, sender=PhaseOneFiles)
def auto_delete_file_on_change1(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_file = PhaseOneFiles.objects.get(pk=instance.pk).receipt_photo
    except PhaseOneFiles.DoesNotExist:
        return False

    new_file = instance.receipt_photo
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)

#some handlers for removing ducuments file for model PhaseOneFiles
@receiver(models.signals.post_delete, sender=PhaseOneFiles)
def auto_delete_file_on_delete2(sender, instance, **kwargs):
    if instance.documents:
        if os.path.isfile(instance.documents.path):
            os.remove(instance.documents.path)

@receiver(models.signals.pre_save, sender=PhaseOneFiles)
def auto_delete_file_on_change2(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_file = PhaseOneFiles.objects.get(pk=instance.pk).documents
    except PhaseOneFiles.DoesNotExist:
        return False

    new_file = instance.documents
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)

#some handlers for removing receipt_photo file for model PhaseTwoFiles
@receiver(models.signals.post_delete, sender=PhaseTwoFiles)
def auto_delete_file_on_delete3(sender, instance, **kwargs):
    if instance.receipt_photo:
        if os.path.isfile(instance.receipt_photo.path):
            os.remove(instance.receipt_photo.path)

@receiver(models.signals.pre_save, sender=PhaseTwoFiles)
def auto_delete_file_on_change3(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_file = PhaseTwoFiles.objects.get(pk=instance.pk).receipt_photo
    except PhaseTwoFiles.DoesNotExist:
        return False

    new_file = instance.receipt_photo
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)



#some handlers for removing functional_document file for model PhaseTwoFiles
@receiver(models.signals.post_delete, sender=PhaseTwoFiles)
def auto_delete_file_on_delete4(sender, instance, **kwargs):
    if instance.functional_document:
        if os.path.isfile(instance.functional_document.path):
            os.remove(instance.functional_document.path)

@receiver(models.signals.pre_save, sender=PhaseTwoFiles)
def auto_delete_file_on_change4(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_file = PhaseTwoFiles.objects.get(pk=instance.pk).functional_document
    except PhaseTwoFiles.DoesNotExist:
        return False

    new_file = instance.functional_document
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)


#some handlers for removing vulnerability_document file for model PhaseTwoFiles
@receiver(models.signals.post_delete, sender=PhaseTwoFiles)
def auto_delete_file_on_delete5(sender, instance, **kwargs):
    if instance.vulnerability_document:
        if os.path.isfile(instance.vulnerability_document.path):
            os.remove(instance.vulnerability_document.path)

@receiver(models.signals.pre_save, sender=PhaseTwoFiles)
def auto_delete_file_on_change5(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_file = PhaseTwoFiles.objects.get(pk=instance.pk).vulnerability_document
    except PhaseTwoFiles.DoesNotExist:
        return False

    new_file = instance.vulnerability_document
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)

#some handlers for removing receipt_photo file for model SupplementFiles
@receiver(models.signals.post_delete, sender=SupplementFiles)
def auto_delete_file_on_delete6(sender, instance, **kwargs):
    if instance.receipt_photo:
        if os.path.isfile(instance.receipt_photo.path):
            os.remove(instance.receipt_photo.path)

@receiver(models.signals.pre_save, sender=SupplementFiles)
def auto_delete_file_on_change6(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_file = SupplementFiles.objects.get(pk=instance.pk).receipt_photo
    except SupplementFiles.DoesNotExist:
        return False

    new_file = instance.receipt_photo
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)

