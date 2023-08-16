from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveDestroyAPIView
from .models import Assessment
from .serializers import AssessmentSerializer
from rest_framework.decorators import api_view, permission_classes


class AssessmentListApiView(ListAPIView):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer
    permission_classes = [IsAuthenticated, ]

class AssessmentRetrieveAPIView(RetrieveDestroyAPIView):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer
    permission_classes = [IsAuthenticated, ]
