from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path('contracts/', ContractListApiView.as_view()),
    path('contracts/<int:pk>', ContractRetrieveAPIView.as_view()),

    path('contracts/contract-photo/<int:id>', manageContractPhoto),
    path('contracts/contract-photo/', manageContractPhoto),

    path('contracts/phase-one/<int:id>', managePhaseOneDocuments),
    path('contracts/phase-one/', managePhaseOneDocuments),

    path('contracts/phase-two/<int:id>', managePhaseTwoDocuments),
    path('contracts/phase-two/', managePhaseTwoDocuments),

    path('contracts/supplement/<int:id>', manageSupplementDocument),
    path('contracts/supplement/', manageSupplementDocument),


    
]
