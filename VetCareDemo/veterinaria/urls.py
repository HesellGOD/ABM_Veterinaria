from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mascotas.urls')),  # 👈 tu app se llama "mascotas"
]