from django.db import models
from django.dispatch import receiver
import os


class Contract(models.Model):
    company_name = models.CharField(max_length=50)
    product_name = models.CharField(max_length=50)
    contract_number = models.CharField(max_length=50, unique=True)
    date_of_contract = models.CharField(max_length=50)
     
    class Meta:
       unique_together = ("company_name", "product_name")


class ContractPhoto(models.Model):
    photo = models.ImageField(upload_to='uploads/')
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE)


@receiver(models.signals.post_delete, sender=ContractPhoto)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.photo:
        if os.path.isfile(instance.photo.path):
            os.remove(instance.photo.path)

@receiver(models.signals.pre_save, sender=ContractPhoto)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
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