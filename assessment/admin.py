from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Contract)
admin.site.register(PhaseOneFiles)
admin.site.register(PhaseTwoFiles)
admin.site.register(SupplementFiles)
admin.site.register(ContractPhoto)