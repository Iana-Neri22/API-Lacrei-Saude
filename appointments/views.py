from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import ProfessionalPerson, Patient, MedicalAppointment
from .serializers import ProfessionalPersonSerializer, PatientSerializer, MedicalAppointmentSerializer

import json


@api_view(['GET'])
def get_professional_persons(request):

    if request.method == 'GET':
        professional_persons = ProfessionalPerson.objects.all()

        serializer = ProfessionalPersonSerializer(professional_persons, many=True)
        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_professional_person_by_id(request, id):

    try:
        professional_person = ProfessionalPerson.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':

        serializer = ProfessionalPersonSerializer(professional_person)
        return Response(serializer.data)
    

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def professional_person_manager(request):

    if request.method == 'GET':

        try:
            if request.GET['professional-person']:

                id = request.GET['professional-person']

                try:
                    professional_person = ProfessionalPerson.objects.get(pk=id)
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                serializer = ProfessionalPersonSerializer(professional_person)
                return Response(serializer.data)
            
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    
    if request.method == 'POST':

        new_professional_person = request.data

        serializer = ProfessionalPersonSerializer(data=new_professional_person)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':

        professional_person = request.data['professional_person_id']

        try:
            updated_professional_person = ProfessionalPerson.objects.get(pk=professional_person)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ProfessionalPersonSerializer(updated_professional_person, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':

        professional_person = request.data['professional_person_id']

        try:
            professional_person_to_delete = ProfessionalPerson.objects.get(pk=professional_person)
            professional_person_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)    