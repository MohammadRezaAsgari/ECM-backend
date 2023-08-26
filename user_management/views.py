import json
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def checkToken(request: Request):
    return JsonResponse({"access": "OK"})

@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def isAdmin(request: Request):
    return JsonResponse({"access": request.user.is_staff})

@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def getUserDetails(request: Request):
    user_username = request.user.username
    return JsonResponse({"username": user_username})

@api_view(['POST'])
@permission_classes([IsAuthenticated,])
def changeUsername(request: Request):
    req_body = json.loads(request.body.decode('utf-8'))
    user_username = req_body['username']
    user_password = req_body['password']
    user = authenticate(request, username=request.user.username, password=user_password)
    if user is not None:
        if user_username==user.username:
            return JsonResponse({"status": "نام کاربری همان نام کاربری قبلی است!", "error":"username same!"})
        if User.objects.filter(username=user_username).exists() and user_username!=user.username:
            return JsonResponse({"status": "حساب با این نام کاربری وجود دارد!", "error":"user exists!"}) 
        user.username = user_username
        user.save()
        return JsonResponse({"status": "نام کاربری با موفقیت تغییر یافت."})
    else:
        return JsonResponse({"status": "پسوورد وارد شده برای این حساب کاربری معتبر نیست!", "error":"password incorrect"})

@api_view(['POST'])
@permission_classes([IsAuthenticated,])
def changeUsernameAndPassword(request: Request):
    req_body = json.loads(request.body.decode('utf-8'))
    user_username = req_body['username']
    user_password = req_body['password']
    user_new_password = req_body['new_password']
    user = authenticate(request, username=request.user.username, password=user_password)
    if user is not None:
        response = JsonResponse({})

        if user.username == user_username:
            response = JsonResponse({"status": "رمز عبور با موفقیت تغییر یافت."})
        else:
            if User.objects.filter(username=user_username).exists():
                return JsonResponse({"status": "حساب با این نام کاربری وجود دارد!", "error":"user exists!"})
            response = JsonResponse({"status": "نام کاربری و رمز عبور با موفقیت تغییر یافت."})
        user.username = user_username
        user.set_password(user_new_password)
        user.save()
        return response
    else:
        return JsonResponse({"status": "پسوورد وارد شده برای این حساب کاربری معتبر نیست!", "error":"password incorrect"})
    

@api_view(['POST'])
@permission_classes([IsAuthenticated,])
def createUser(request: Request):
    req_body = json.loads(request.body.decode('utf-8'))
    user_username = req_body['username']
    user_password = req_body['password']
    user_isadmin = req_body['isAdmin']
    if User.objects.filter(username=user_username).exists():
        return JsonResponse({"status": "حساب با این نام کاربری وجود دارد!", "error":"user exists!"})
    else:
        User.objects.create_user(username=user_username,password=user_password, is_staff=user_isadmin)
        return JsonResponse({"status": "کاربر ایجاد شد."})