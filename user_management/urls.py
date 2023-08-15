from django.urls import path, include
from .views import *

urlpatterns = [
    path('login/', loginView, name='login'),
    path('logout/', logoutView),
    path('test/', test),
    path('checktoken/', checkToken),
]
