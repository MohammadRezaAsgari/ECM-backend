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


class ContractListCreateApiView(ListCreateAPIView):
    queryset = Contract.objects.all().order_by('-id').values()
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated, ]
    filter_backends = [filters.SearchFilter , ]
    search_fields = ['contract_number', 'company_name' , 'product_name']


class ContractRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated, ]



# Contract first Page Photo
@api_view(['GET', 'POST', 'PUT',])
@permission_classes([IsAuthenticated])
def manageContractPhoto(request: Request, id: int = None):
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
 

#Phase one docs    
@api_view(['GET', 'POST', 'PUT',])
@permission_classes([IsAuthenticated])
def managePhaseOneDocuments(request: Request, id: int = None):
    if request.method == 'GET':
        if id == None : 
            return HttpResponse(status=status.HTTP_403_FORBIDDEN)
        
        if PhaseOneDocument.objects.filter(contract__id=id).exists():
            phaseOne_document = PhaseOneDocument.objects.get(contract__id=id)
            return HttpResponse(phaseOne_document.documents, content_type="application/x-zip-compressed")
        return JsonResponse({"response": "Not exists"})
    
    if request.method == 'POST':
        contract = Contract.objects.get(id=request.POST['post_id'])
        PhaseOneDocument.objects.create(documents=request.FILES["documents"], contract=contract)
        return HttpResponse(status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        if id == None : 
            return HttpResponse(status=status.HTTP_403_FORBIDDEN)
        phaseOne_document = PhaseOneDocument.objects.get(contract__id=id)
        phaseOne_document.documents = request.FILES["documents"]
        phaseOne_document.save()
        return HttpResponse(status=status.HTTP_200_OK)


#Phase two docs    
@api_view(['GET', 'POST', 'PUT',])
@permission_classes([IsAuthenticated])
def managePhaseTwoDocuments(request: Request, id: int = None):
    if request.method == 'GET':
        if id == None : 
            return HttpResponse(status=status.HTTP_403_FORBIDDEN)
        
        if PhaseTwoDocument.objects.filter(contract__id=id).exists():
            phaseTwo_document = PhaseTwoDocument.objects.get(contract__id=id)
            return HttpResponse(phaseTwo_document.documents, content_type="application/x-zip-compressed")
        return JsonResponse({"response": "Not exists"})
    
    if request.method == 'POST':
        contract = Contract.objects.get(id=request.POST['post_id'])
        PhaseTwoDocument.objects.create(documents=request.FILES["documents"], contract=contract)
        return HttpResponse(status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        if id == None : 
            return HttpResponse(status=status.HTTP_403_FORBIDDEN)
        phaseTwo_document = PhaseTwoDocument.objects.get(contract__id=id)
        phaseTwo_document.documents = request.FILES["documents"]
        phaseTwo_document.save()
        return HttpResponse(status=status.HTTP_200_OK)


#Supplement files    
@api_view(['GET', 'POST', 'PUT',])
@permission_classes([IsAuthenticated])
def manageSupplementDocument(request: Request, id: int = None):
    if request.method == 'GET':
        if id == None : 
            return HttpResponse(status=status.HTTP_403_FORBIDDEN)
        
        if SupplementDocument.objects.filter(contract__id=id).exists():
            supplement_file = SupplementDocument.objects.get(contract__id=id)
            return HttpResponse(supplement_file.receipt_photo, content_type="image/jpeg")
        return JsonResponse({"response": "Not exists"})
    
    if request.method == 'POST':
        contract = Contract.objects.get(id=request.POST['post_id'])
        SupplementDocument.objects.create(receipt_photo=request.FILES["photo"], contract=contract)
        return HttpResponse(status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        if id == None : 
            return HttpResponse(status=status.HTTP_403_FORBIDDEN)
        supplement_file = SupplementDocument.objects.get(contract__id=id)
        supplement_file.receipt_photo = request.FILES["photo"]
        supplement_file.save()
        return HttpResponse(status=status.HTTP_200_OK)
    