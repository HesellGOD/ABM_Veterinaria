from django.urls import path, include
from rest_framework import routers
from .views import DueñoViewSet, MascotaViewSet, VisitaViewSet

router = routers.DefaultRouter()
router.register('dueños', DueñoViewSet)
router.register('mascotas', MascotaViewSet)
router.register('visitas', VisitaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]