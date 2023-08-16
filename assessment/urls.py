from django.urls import path, include
from .views import *

urlpatterns = [
    path('assessments/', AssessmentListApiView.as_view()),
    path('assessments/<int:pk>', AssessmentRetrieveAPIView.as_view()),
]
