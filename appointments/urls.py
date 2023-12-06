from django.contrib import admin
from django.urls import path, include

from .import views

urlpatterns = [
    path('', views.get_professional_persons, name='get_all_professional_persons'),
    path('professional-person/<int:id', views.get_professional_person_by_id),
    path('data/', views.professional_person_manager)
]


