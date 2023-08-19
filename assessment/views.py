from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Assessment
from .serializers import AssessmentSerializer
from rest_framework.decorators import api_view, permission_classes
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .search_filters import CustomSearchFilter
from rest_framework.decorators import api_view,permission_classes

class AssessmentListApiView(ListCreateAPIView):
    queryset = Assessment.objects.all().order_by('-id').values()
    serializer_class = AssessmentSerializer
    permission_classes = [IsAuthenticated, ]
    #filter_backends = [CustomSearchFilter]
    #search_fields = ['company_name', 'product_name', 'contract_number']


class AssessmentRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer
    permission_classes = [IsAuthenticated, ]


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getPhoto(request: Request, contract_num: int):
    assessment = Assessment.objects.all().get(contract_number=contract_num)
    with open(f'./uploads/{contract_num}', "rb") as f:
        return HttpResponse(f.read(), content_type="image/jpeg")
        

    
