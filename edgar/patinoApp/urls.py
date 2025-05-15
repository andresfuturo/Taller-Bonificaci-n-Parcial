from django.urls import path
from .views import PacienteListView, PacienteCreateView, PacienteUpdateView, PacienteDeleteView, CitaListView, CitaCreateView, CitaUpdateView, CitaDeleteView

urlpatterns = [
    path('', PacienteListView.as_view(), name='paciente-list'),
    path('nuevo/', PacienteCreateView.as_view(), name='paciente-create'),
    path('editar/<int:pk>/', PacienteUpdateView.as_view(), name='paciente-update'),
    path('eliminar/<int:pk>/', PacienteDeleteView.as_view(), name='paciente-delete'),

    path('citas/', CitaListView.as_view(), name='cita-list'),
    path('citas/nueva/', CitaCreateView.as_view(), name='cita-create'),
    path('citas/editar/<int:pk>/', CitaUpdateView.as_view(), name='cita-update'),
    path('citas/eliminar/<int:pk>/', CitaDeleteView.as_view(), name='cita-delete'),
]
