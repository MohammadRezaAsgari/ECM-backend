from django.urls import path, include
from .views import *

urlpatterns = [
    path('checktoken/', checkToken),
    path('isAdmin/', isAdmin),
    path('getusername/', getUserDetails),
    path('changeusername/', changeUsername),
    path('changeuserpass/', changeUsernameAndPassword),
    path('createuser/', createUser),
]
