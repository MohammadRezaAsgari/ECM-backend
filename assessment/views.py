from django.http import HttpResponse, JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework import status, filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view, permission_classes
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view,permission_classes
from .models import *
from .serializers import *
from .search_filters import CustomSearchFilter


class ContractListApiView(ListCreateAPIView):
    queryset = Contract.objects.all().order_by('-id').values()
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated, ]
    filter_backends = [filters.SearchFilter , ]
    search_fields = ['contract_number', 'company_name' , 'product_name']


class ContractRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated, ]


@api_view(['GET', 'POST', 'PUT',])
@permission_classes([IsAuthenticated])
def managePhoto(request: Request, id: int = None):

    if request.method == 'GET':
        if id == None : 
            return HttpResponse(status=status.HTTP_403_FORBIDDEN)
        
        if ContractPhoto.objects.filter(contract__id=id).exists():
            contract_photo = ContractPhoto.objects.get(contract__id=id)
            return HttpResponse(contract_photo.photo, content_type="image/jpeg")
        return JsonResponse({"response": "Not exists"})
    
    if request.method == 'POST':
        contract = Contract.objects.get(id=request.POST['post_id'])
        ContractPhoto.objects.create(photo=request.FILES["photo"], contract=contract)
        return HttpResponse(status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        if id == None : 
            return HttpResponse(status=status.HTTP_403_FORBIDDEN)
        contract_photo = ContractPhoto.objects.get(contract__id=id)
        contract_photo.photo = request.FILES["photo"]
        contract_photo.save()
        return HttpResponse(status=status.HTTP_200_OK)
 
    