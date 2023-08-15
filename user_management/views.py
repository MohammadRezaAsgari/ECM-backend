from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes

@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def checkToken(request: Request):
    return JsonResponse({"access": "OK"})
