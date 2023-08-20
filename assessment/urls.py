from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path('assessments/', AssessmentListApiView.as_view()),
    path('assessments/<int:pk>', AssessmentRetrieveAPIView.as_view()),
    path('assessments/photo/<int:id>', managePhoto),
]
