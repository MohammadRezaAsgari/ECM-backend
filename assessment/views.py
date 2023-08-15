from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from .models import Assessment
from .serializers import AssessmentSerializer
from rest_framework.decorators import api_view, permission_classes


# @api_view(['GET'])
# @permission_classes([IsAuthenticated,])
def assessmentsListView(request: Request):
    serialized_data = AssessmentSerializer(Assessment.objects.all())
    return Response(serialized_data.data, status=status.HTTP_200_OK)

class AssessmentListApiView(ListAPIView):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer
    #permission_classes = [IsAuthenticated, ]
