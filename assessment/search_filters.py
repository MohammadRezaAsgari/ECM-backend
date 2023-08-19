from rest_framework import filters

class CustomSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        if request.query_params.get('company_name'):
            return ['company_name']
        if request.query_params.get('product_name'):
            return ['product_name']
        if request.query_params.get('contract_number'):
            return ['^contract_number']
        return super().get_search_fields(view, request)