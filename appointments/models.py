from django.db import models


class ProfessionalPerson(models.Model):
    professional_person_id = models.IntegerField(primary_key=True)
    professional_person_social_name = models.CharField(max_length=150, default='')

    def __str__(self):
        return f'Id da Pessoa Profissional: {self.professional_person_id} | Pessoa Profissional: {self.professional_person_social_name}'


class Patient(models.Model):
    patient_id = models.IntegerField(primary_key=True)
    patient_social_name = models.CharField(max_length=150, default='')

    def __str__(self):
        return f'Id paciente: {self.patient_id} | Paciente: {self.patient_social_name}'


class MedicalAppointment(models.Model):
    medical_appointment_id = models.IntegerField(primary_key=True)
    professional_person = models.ForeignKey(ProfessionalPerson, on_delete=models.DO_NOTHING)
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    appointment_date = models.DateField()

    def __str__(self):
        return f'Id da Consulta Médica: {self.medical_appointment_id} | Id da Pessoa Profissional: {self.professional_person_id} | Id paciente: {self.patient_id} | Data da Consulta: {self.appointment_date}'






