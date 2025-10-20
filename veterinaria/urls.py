from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from mascotas.views import DueñoViewSet, MascotaViewSet, VisitaViewSet

router = routers.DefaultRouter()
router.register(r'dueños', DueñoViewSet)
router.register(r'mascotas', MascotaViewSet)
router.register(r'visitas', VisitaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
