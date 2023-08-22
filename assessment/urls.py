from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path('contracts/', ContractListApiView.as_view()),
    path('contracts/<int:pk>', ContractRetrieveAPIView.as_view()),
    path('contracts/photo/<int:id>', managePhoto),
    path('contracts/photo/', managePhoto),
]
