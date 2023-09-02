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
 


#Phase 1 files
@api_view(['GET',])
@permission_classes([IsAuthenticated])
def getPhaseOneReceiptPhoto(request: Request, id: int = None):
    if request.method == 'GET':
        if id == None : 
            return HttpResponse(status=status.HTTP_403_FORBIDDEN)
        
        if PhaseOneFiles.objects.filter(contract__id=id).exists():
            phase_one_file = PhaseOneFiles.objects.get(contract__id=id)
            return HttpResponse(phase_one_file.receipt_photo, content_type="image/jpeg")
        return JsonResponse({"response": "Not exists"})
    
@api_view(['GET',])
@permission_classes([IsAuthenticated])
def getPhaseOneDocuments(request: Request, id: int = None):
    if request.method == 'GET':
        if id == None : 
            return HttpResponse(status=status.HTTP_403_FORBIDDEN)
        
        if PhaseOneFiles.objects.filter(contract__id=id).exists():
            phase_one_file = PhaseOneFiles.objects.get(contract__id=id)
            return HttpResponse(phase_one_file.documents, content_type="application/x-zip-compressed")
        return JsonResponse({"response": "Not exists"})
    
@api_view(['POST', 'PUT', ])
@permission_classes([IsAuthenticated])
def createUpdatePhaseOneFiles(request: Request, id: int = None):    
    if request.method == 'POST':
        contract = Contract.objects.get(id=request.POST['post_id'])
        PhaseOneFiles.objects.create(receipt_photo=request.FILES["receipt_photo"] ,documents=request.FILES["documents"] , contract=contract)
        return HttpResponse(status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        if id == None : 
            return HttpResponse(status=status.HTTP_403_FORBIDDEN)
        phase_one_file = PhaseOneFiles.objects.get(contract__id=id)
        phase_one_file.receipt_photo = request.FILES["receipt_photo"]
        phase_one_file.documents = request.FILES["documents"]
        phase_one_file.save()
        return HttpResponse(status=status.HTTP_200_OK)
 
        



# Phase 2 files
@api_view(['GET',])
@permission_classes([IsAuthenticated])
def getPhaseTwoReceiptPhoto(request: Request, id: int = None):
    if request.method == 'GET':
        if id == None : 
            return HttpResponse(status=status.HTTP_403_FORBIDDEN)
        
        if PhaseTwoFiles.objects.filter(contract__id=id).exists():
            phase_two_file = PhaseTwoFiles.objects.get(contract__id=id)
            return HttpResponse(phase_two_file.receipt_photo, content_type="image/jpeg")
        return JsonResponse({"response": "Not exists"})
    
@api_view(['GET',])
@permission_classes([IsAuthenticated])
def getPhaseTwoFuncDocuments(request: Request, id: int = None):
    if request.method == 'GET':
        if id == None : 
            return HttpResponse(status=status.HTTP_403_FORBIDDEN)
        
        if PhaseTwoFiles.objects.filter(contract__id=id).exists():
            phase_two_file = PhaseTwoFiles.objects.get(contract__id=id)
            return HttpResponse(phase_two_file.functional_document, content_type="application/x-zip-compressed")
        return JsonResponse({"response": "Not exists"})
    
@api_view(['GET',])
@permission_classes([IsAuthenticated])
def getPhaseTwoVulDocuments(request: Request, id: int = None):
    if request.method == 'GET':
        if id == None : 
            return HttpResponse(status=status.HTTP_403_FORBIDDEN)
        
        if PhaseTwoFiles.objects.filter(contract__id=id).exists():
            phase_two_file = PhaseTwoFiles.objects.get(contract__id=id)
            return HttpResponse(phase_two_file.vulnerability_document, content_type="application/x-zip-compressed")
        return JsonResponse({"response": "Not exists"})
    
@api_view(['POST', 'PUT', ])
@permission_classes([IsAuthenticated])
def createUpdatePhaseTwoFiles(request: Request, id: int = None):    
    if request.method == 'POST':
        contract = Contract.objects.get(id=request.POST['post_id'])
        PhaseTwoFiles.objects.create(receipt_photo=request.FILES["receipt_photo"] ,functional_document=request.FILES["functional_document"] , vulnerability_document=request.FILES["vulnerability_document"], contract=contract)
        return HttpResponse(status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        if id == None : 
            return HttpResponse(status=status.HTTP_403_FORBIDDEN)
        phase_two_file = PhaseTwoFiles.objects.get(contract__id=id)
        phase_two_file.receipt_photo = request.FILES["receipt_photo"]
        phase_two_file.functional_document = request.FILES["functional_document"]
        phase_two_file.vulnerability_document = request.FILES["vulnerability_document"]
        phase_two_file.save()
        return HttpResponse(status=status.HTTP_200_OK)


#Supplement files    
@api_view(['GET', 'POST', 'PUT',])
@permission_classes([IsAuthenticated])
def manageSupplementFiles(request: Request, id: int = None):
    if request.method == 'GET':
        if id == None : 
            return HttpResponse(status=status.HTTP_403_FORBIDDEN)
        
        if SupplementFiles.objects.filter(contract__id=id).exists():
            supplement_file = SupplementFiles.objects.get(contract__id=id)
            return HttpResponse(supplement_file.receipt_photo, content_type="image/jpeg")
        return JsonResponse({"response": "Not exists"})
    
    if request.method == 'POST':
        contract = Contract.objects.get(id=request.POST['post_id'])
        SupplementFiles.objects.create(receipt_photo=request.FILES["receipt_photo"], contract=contract)
        return HttpResponse(status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        if id == None : 
            return HttpResponse(status=status.HTTP_403_FORBIDDEN)
        supplement_file = SupplementFiles.objects.get(contract__id=id)
        supplement_file.receipt_photo = request.FILES["receipt_photo"]
        supplement_file.save()
        return HttpResponse(status=status.HTTP_200_OK)