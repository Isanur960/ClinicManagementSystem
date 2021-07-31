from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index.as_view(), name='Index'),
    path('add-patient', views.addPatient.as_view(), name='Add-Patient'),
    path('patient-list', views.patientList.as_view(), name='Patient-List'),
    path('edit', views.editPatient.as_view(), name='Edit'),
    path('delete', views.deletePatient.as_view(), name='Delete'),
]
