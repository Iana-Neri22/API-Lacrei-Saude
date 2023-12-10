from django.contrib import admin
from django.urls import path, include

from .import views

urlpatterns = [
    path('professional-person/', views.professional_person_manager),
    path('patient/', views.patient_manager),
    path('medical-appointment/', views.medical_appointment_manager)
]


