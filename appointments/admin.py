from django.contrib import admin

from .models import ProfessionalPerson, Patient, MedicalAppointment

admin.site.register(ProfessionalPerson)
admin.site.register(Patient)
admin.site.register(MedicalAppointment)
