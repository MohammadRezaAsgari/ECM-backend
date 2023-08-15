from rest_framework import serializers
from .models import Assessment

class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = [ 'id' , 'product_name' , 'company_name' , 'contract_number' , 'data_of_contract']
