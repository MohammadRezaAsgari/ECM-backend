from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Contract)
admin.site.register(ContractPhoto)
admin.site.register(PhaseOneDocument)
admin.site.register(PhaseTwoDocument)
admin.site.register(SupplementDocument)