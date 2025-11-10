from django.urls import path, include
from django.contrib.auth.views import LogoutView
from rest_framework import routers
from .views import (
    IndexView, exportar_pdf, CustomLoginView,
    DueñoViewSet, MascotaViewSet, VisitaViewSet,
    DueñoListView, DueñoCreateView, DueñoUpdateView, DueñoDeleteView,
    MascotaListView, MascotaCreateView, MascotaUpdateView, MascotaDetailView, MascotaDeleteView,
    VisitaListView, VisitaCreateView, VisitaUpdateView, VisitaDetailView, VisitaDeleteView
)

router = routers.DefaultRouter()
router.register(r'dueños', DueñoViewSet)
router.register(r'mascotas', MascotaViewSet)
router.register(r'visitas', VisitaViewSet)

urlpatterns = [
    # Autenticación
    path('inicio/', IndexView.as_view(), name='index'),
    path('', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('api/', include(router.urls)),

    # ===================
    # DUEÑOS
    # ===================
    path('dueños/', DueñoListView.as_view(), name='dueño_list'),
    path('dueños/nuevo/', DueñoCreateView.as_view(), name='dueño_create'),
    path('dueños/<int:pk>/editar/', DueñoUpdateView.as_view(), name='dueño_edit'),
    path('dueños/<int:pk>/eliminar/', DueñoDeleteView.as_view(), name='dueño_delete'),

    # ===================
    # MASCOTAS
    # ===================
    path('mascotas/', MascotaListView.as_view(), name='mascota_list'),
    path('mascotas/nueva/', MascotaCreateView.as_view(), name='mascota_create'),
    path('mascotas/<int:pk>/editar/', MascotaUpdateView.as_view(), name='mascota_edit'),
    path('mascotas/<int:pk>/', MascotaDetailView.as_view(), name='mascota_detail'),
    path('mascotas/<int:pk>/eliminar/', MascotaDeleteView.as_view(), name='mascota_delete'),
    path('mascotas/<int:pk>/pdf/', exportar_pdf, name='exportar_pdf'),

    # ===================
    # VISITAS
    # ===================
    path('visitas/', VisitaListView.as_view(), name='visita_list'),
    path('visitas/nueva/', VisitaCreateView.as_view(), name='visita_create'),
    path('visitas/<int:pk>/editar/', VisitaUpdateView.as_view(), name='visita_edit'),
    path('visitas/<int:pk>/', VisitaDetailView.as_view(), name='visita_detail'),
    path('visitas/<int:pk>/eliminar/', VisitaDeleteView.as_view(), name='visita_delete'),
]
