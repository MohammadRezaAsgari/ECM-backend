from rest_framework import serializers
from .models import *


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = [ 'id' , 'product_name' , 'company_name' , 'contract_number' , 'date_of_contract'  ]
