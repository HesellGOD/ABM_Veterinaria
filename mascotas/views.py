from rest_framework import viewsets
from .models import Dueño, Mascota, Visita
from .serializers import DueñoSerializer, MascotaSerializer, VisitaSerializer
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .forms import DueñoForm, MascotaForm, VisitaForm
class DueñoViewSet(viewsets.ModelViewSet):
    queryset = Dueño.objects.all()
    serializer_class = DueñoSerializer

class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer

class VisitaViewSet(viewsets.ModelViewSet):
    queryset = Visita.objects.all()
    serializer_class = VisitaSerializer

# ===========================
#        DUEÑOS
# ===========================
class DueñoListView(ListView):
    model = Dueño
    template_name = 'dueño_list.html'
    context_object_name = 'dueños'
    ordering = ['nombre']


class DueñoCreateView(CreateView):
    model = Dueño
    form_class = DueñoForm
    template_name = 'dueño_form.html'
    success_url = reverse_lazy('dueño_list')


class DueñoUpdateView(UpdateView):
    model = Dueño
    form_class = DueñoForm
    template_name = 'dueño_form.html'
    success_url = reverse_lazy('dueño_list')


# ===========================
#        MASCOTAS
# ===========================
class MascotaListView(ListView):
    model = Mascota
    template_name = 'mascota_list.html'
    context_object_name = 'mascotas'
    ordering = ['nombre']


class MascotaCreateView(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota_form.html'
    success_url = reverse_lazy('mascota_list')


class MascotaUpdateView(UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota_form.html'
    success_url = reverse_lazy('mascota_list')


class MascotaDetailView(DetailView):
    model = Mascota
    template_name = 'mascota_detail.html'
    context_object_name = 'mascota'


# ===========================
#        VISITAS
# ===========================
class VisitaListView(ListView):
    model = Visita
    template_name = 'visita_list.html'
    context_object_name = 'visitas'
    ordering = ['-fecha']


class VisitaCreateView(CreateView):
    model = Visita
    form_class = VisitaForm
    template_name = 'visita_form.html'
    success_url = reverse_lazy('visita_list')


class VisitaUpdateView(UpdateView):
    model = Visita
    form_class = VisitaForm
    template_name = 'visita_form.html'
    success_url = reverse_lazy('visita_list')


class VisitaDetailView(DetailView):
    model = Visita
    template_name = 'visita_detail.html'
    context_object_name = 'visita'
