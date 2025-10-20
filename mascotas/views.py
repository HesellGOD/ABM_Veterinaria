from rest_framework import viewsets
from .models import Dueño, Mascota, Visita
from .serializers import DueñoSerializer, MascotaSerializer, VisitaSerializer

class DueñoViewSet(viewsets.ModelViewSet):
    queryset = Dueño.objects.all()
    serializer_class = DueñoSerializer

class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer

class VisitaViewSet(viewsets.ModelViewSet):
    queryset = Visita.objects.all()
    serializer_class = VisitaSerializer

