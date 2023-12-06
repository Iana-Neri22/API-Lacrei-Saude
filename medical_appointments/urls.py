from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lacrei-saude/', include('appointments.urls'), name='medical_appointments_urls')
]


