from rest_framework.request import Request
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from .serializers import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes

def loginView2(request: Request):
    if request.method == "POST":
        serialized_data = LoginSerializer(data=request.POST)
        serialized_data.is_valid()

        username = serialized_data.validated_data.get("username")
        password = serialized_data.validated_data.get("password")

        if not User.objects.filter(username=username).exists():
            return render(request, "login.html", {"massage": "کاربر تعریف نشده است."})

        user = authenticate(request, username=username, password=password)
        if not user:
            return render(
                request, "login.html", {"massage": "رمز عبور شما صحیح نمیباشد."}
            )

        login(request, user)
        return HttpResponseRedirect(reverse("home", current_app="assessment"))

    return render(request, "login.html", {"massage": ""})


def logoutView(request: Request):
    if request.method == "GET":
        logout(request)
        return HttpResponseRedirect(reverse("login"))
    
    
# @api_view(['GET'])
# @permission_classes([IsAuthenticated,])
def test(request: Request):
    if request.method == "GET":
        return JsonResponse({"foo": "bar", "foo3": "bar3"})



def loginView(request: Request):
    if request.method == "POST":
        serialized_data = LoginSerializer(data=request.POST)
        serialized_data.is_valid()

        username = serialized_data.validated_data.get("username")
        password = serialized_data.validated_data.get("password")
        print(username)
        return HttpResponse("login okeye")
    return HttpResponse("login kon")
