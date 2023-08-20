from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Assessment, AssessmentPhoto
from .serializers import AssessmentSerializer
from rest_framework.decorators import api_view, permission_classes
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .search_filters import CustomSearchFilter
from rest_framework.decorators import api_view,permission_classes
import os
from django.http import JsonResponse

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


@api_view(['GET', 'POST', 'PUT'])
@permission_classes([IsAuthenticated])
def managePhoto(request: Request, id: int):

    if request.method == 'GET':
        assessment = Assessment.objects.all().get(id=id)
        if assessment.contract_photo:
            return HttpResponse(assessment.contract_photo.photo, content_type="image/jpeg")
        return JsonResponse({"response": "Not exists"})
    
    if request.method == 'POST':
        assessment = Assessment.objects.all().get(id=id)
        #assessment_photo = AssessmentPhoto.objects.create(photo=request.FILES["photo"])
        print(request.FILES["photo"])