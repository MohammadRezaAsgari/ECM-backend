from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path('contracts/', ContractListApiView.as_view()),
    path('contracts/<int:pk>', ContractRetrieveAPIView.as_view()),
    path('contracts/contract-photo/<int:id>', manageContractPhoto),
    path('contracts/contract-photo/', manageContractPhoto),

    path('contracts/receipt-photo/phase-one/<int:id>', getPhaseOneReceiptPhoto ),
    path('contracts/receipt-photo/phase-two/<int:id>', getPhaseTwoReceiptPhoto ),
    path('contracts/documents/phase-one/<int:id>', getPhaseOneDocuments),
    path('contracts/fdocuments/phase-two/<int:id>', getPhaseTwoFuncDocuments),
    path('contracts/vdocuments/phase-two/<int:id>', getPhaseTwoVulDocuments),

    path('contracts/phase-one/', createUpdatePhaseOneFiles),
    path('contracts/phase-two/', createUpdatePhaseTwoFiles),
    path('contracts/phase-one/<int:id>', createUpdatePhaseOneFiles),
    path('contracts/phase-two/<int:id>', createUpdatePhaseTwoFiles),
    
    path('contracts/supplement/<int:id>', manageSupplementFiles),
    path('contracts/supplement/', manageSupplementFiles),

]
