from django.urls import path, include
from .views import *

urlpatterns = [
    path('assessments/', assessmentsListView, name='home'),
]
