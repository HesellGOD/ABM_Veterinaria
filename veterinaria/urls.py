from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from mascotas.views import DueñoViewSet, MascotaViewSet, VisitaViewSet
from mascotas.views import (
    DueñoListView, DueñoCreateView, DueñoUpdateView,
    MascotaListView, MascotaCreateView, MascotaUpdateView, MascotaDetailView,
    VisitaListView, VisitaCreateView, VisitaUpdateView, VisitaDetailView
)

router = routers.DefaultRouter()
router.register(r'dueños', DueñoViewSet)
router.register(r'mascotas', MascotaViewSet)
router.register(r'visitas', VisitaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    # ===================
    # DUEÑOS
    # ===================
    path('dueños/', DueñoListView.as_view(), name='dueño_list'),
    path('dueños/nuevo/', DueñoCreateView.as_view(), name='dueño_create'),
    path('dueños/<int:pk>/editar/', DueñoUpdateView.as_view(), name='dueño_edit'),

    # ===================
    # MASCOTAS
    # ===================
    path('mascotas/', MascotaListView.as_view(), name='mascota_list'),
    path('mascotas/nueva/', MascotaCreateView.as_view(), name='mascota_create'),
    path('mascotas/<int:pk>/editar/', MascotaUpdateView.as_view(), name='mascota_edit'),
    path('mascotas/<int:pk>/', MascotaDetailView.as_view(), name='mascota_detail'),

    # ===================
    # VISITAS
    # ===================
    path('visitas/', VisitaListView.as_view(), name='visita_list'),
    path('visitas/nueva/', VisitaCreateView.as_view(), name='visita_create'),
    path('visitas/<int:pk>/editar/', VisitaUpdateView.as_view(), name='visita_edit'),
    path('visitas/<int:pk>/', VisitaDetailView.as_view(), name='visita_detail'),
]
