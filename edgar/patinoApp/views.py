from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Paciente, Cita

class PacienteListView(ListView):
    model = Paciente
    template_name = 'html/paciente_list.html'

class PacienteCreateView(CreateView):
    model = Paciente
    fields = ['nombre', 'email']
    template_name = 'html/paciente_form.html'
    success_url = reverse_lazy('paciente-list')

class PacienteUpdateView(UpdateView):
    model = Paciente
    fields = ['nombre', 'email']
    template_name = 'html/paciente_form.html'
    success_url = reverse_lazy('paciente-list')

class PacienteDeleteView(DeleteView):
    model = Paciente
    template_name = 'html/paciente_confirm_delete.html'
    success_url = reverse_lazy('paciente-list')


class CitaListView(ListView):
    model = Cita
    template_name = 'html/cita_list.html'

class CitaCreateView(CreateView):
    model = Cita
    fields = ['paciente', 'fecha', 'descripcion']
    template_name = 'html/cita_form.html'
    success_url = reverse_lazy('cita-list')

class CitaUpdateView(UpdateView):
    model = Cita
    fields = ['paciente', 'fecha', 'descripcion']
    template_name = 'html/cita_form.html'
    success_url = reverse_lazy('cita-list')

class CitaDeleteView(DeleteView):
    model = Cita
    template_name = 'html/cita_confirm_delete.html'
    success_url = reverse_lazy('cita-list')
