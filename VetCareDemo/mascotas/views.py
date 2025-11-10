from rest_framework import viewsets
from .models import Dueño, Mascota, Visita
from .serializers import DueñoSerializer, MascotaSerializer, VisitaSerializer
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .forms import DueñoForm, MascotaForm, VisitaForm
from io import BytesIO
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.utils import timezone
from datetime import datetime, timedelta
from django.db.models import Sum

class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

    def get_success_url(self):
        return self.success_url

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Total de mascotas registradas
        context['total_mascotas'] = Mascota.objects.count()
        
        # Turnos del día actual
        hoy = timezone.now()
        inicio_dia = hoy.replace(hour=0, minute=0, second=0, microsecond=0)
        fin_dia = hoy.replace(hour=23, minute=59, second=59, microsecond=999999)
        
        context['turnos_pendientes'] = Visita.objects.filter(
            fecha__gte=hoy,
            estado='pendiente'
        ).count()
        
        # Próximos turnos (ordenados por fecha, limitados a 3)
        context['proximos_turnos'] = Visita.objects.filter(
            fecha__gte=hoy,
            estado='pendiente'
        ).select_related('mascota', 'mascota__dueño').order_by('fecha')[:3]
        
        return context
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
    
    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q', '').strip()
        if q:
            qs = qs.filter(nombre__icontains=q)
        return qs.order_by('nombre')


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

class DueñoDeleteView(DeleteView):
    model = Dueño
    template_name = 'dueño_delete.html'
    success_url = reverse_lazy('dueño_list')

# ===========================
#        MASCOTAS
# ===========================
class MascotaListView(ListView):
    model = Mascota
    template_name = 'mascota_list.html'
    context_object_name = 'mascotas'
    ordering = ['nombre']

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q', '').strip()
        if q:
            qs = qs.filter(nombre__icontains=q)
        return qs.order_by('nombre')

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

class MascotaDeleteView(DeleteView):
    model = Mascota
    template_name = 'mascota_delete.html'
    success_url = reverse_lazy('mascota_list')

# ===========================
#        VISITAS
# ===========================
class VisitaListView(ListView):
    model = Visita
    template_name = 'visita_list.html'
    context_object_name = 'visitas'
    ordering = ['-fecha']

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q', '').strip()
        if q:
            # Buscar por nombre de la mascota
            qs = qs.filter(mascota__nombre__icontains=q)
        return qs.order_by('-fecha')

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

def exportar_pdf(request, pk):
    # Obtener la mascota
    mascota = get_object_or_404(Mascota, pk=pk)
    
    # Cargar el template
    template = get_template('pdf/mascota_pdf.html')
    context = {'mascota': mascota}
    
    # Renderizar el HTML
    html = template.render(context)
    
    # Crear el PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="ficha_mascota_{mascota.nombre}.pdf"'
    
    # Generar PDF
    buffer = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), buffer)
    
    if not pdf.err:
        # Si todo está bien, devolver el PDF
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response
    
    # Si hay error, devolver el error en texto plano
    return HttpResponse("Error al generar el PDF", content_type='text/plain')

class VisitaDeleteView(DeleteView):
    model = Visita
    template_name = 'visita_delete.html'
    success_url = reverse_lazy('visita_list')