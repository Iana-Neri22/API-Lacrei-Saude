from rest_framework import serializers

from .models import ProfessionalPerson, Patient, MedicalAppointment


class ProfessionalPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalPerson
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class MedicalAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalAppointment
        fields = '__all__'