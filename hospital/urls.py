from django.urls import path
from .views import recover_username
from .views import (
    home, patient_list, doctor_list, appointment_list, appointment_detail, 
    appointment_create, appointment_update, appointment_delete,
    medical_record_list, medical_record_detail, medical_record_create, add_patient
)

urlpatterns = [
    path('recover-username/', recover_username, name='recover_username'),
    path('', home, name='home'), 
    path('patients/', patient_list, name='patient_list'),
    path('patients/add/', add_patient, name='add_patient'),  # Add patient URL
    path('doctors/', doctor_list, name='doctor_list'),
    path('appointments/', appointment_list, name='appointment_list'),
    path('appointments/<int:pk>/', appointment_detail, name='appointment_detail'),
    path('appointments/new/', appointment_create, name='appointment_create'),
    path('appointments/<int:pk>/edit/', appointment_update, name='appointment_update'),
    path('appointments/<int:pk>/delete/', appointment_delete, name='appointment_delete'),
    path('records/', medical_record_list, name='medical_record_list'),
    path('records/<int:pk>/', medical_record_detail, name='medical_record_detail'),
    path('records/new/', medical_record_create, name='medical_record_create'),
]

