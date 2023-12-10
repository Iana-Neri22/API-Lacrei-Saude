from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import ProfessionalPerson, Patient, MedicalAppointment
from .serializers import ProfessionalPersonSerializer, PatientSerializer, MedicalAppointmentSerializer
from .api_functions import entity_manager


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def professional_person_manager(request):
    return entity_manager(request, 'professional-person', ProfessionalPerson, ProfessionalPersonSerializer, 'professional_person_id')

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def patient_manager(request):
    return entity_manager(request, 'patient', Patient, PatientSerializer, 'patient_id')

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def medical_appointment_manager(request):
    return entity_manager(request, 'medical-appointment', MedicalAppointment, MedicalAppointmentSerializer, 'medical_appointment_id')

