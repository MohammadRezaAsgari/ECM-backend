from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.request import Request
from .models import Assessment
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.views.decorators.cache import cache_control


base_url = 'http://127.0.0.1:8000'
log_out_url = base_url + '/api/usermanagement/logout/'
home_url = base_url + '/api/assessment/assessments/'
create_assessment_url = base_url + '/api/assessment/create/'

@api_view(['GET'])
@cache_control(no_cache=True, must_revalidate=True)
@authentication_classes([SessionAuthentication])
def assessmentsListView(request: Request):
    if request.user and request.user.is_authenticated:
        return render(request, 'home.html',{'assessments': Assessment.objects.all() , 'logouturl':log_out_url, 'home_url':home_url, 'create_assessment_url':create_assessment_url})
    else:
        return HttpResponseRedirect(reverse("login"))
    

