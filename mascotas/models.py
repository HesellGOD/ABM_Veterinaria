from django.db import models
from datetime import date
from dateutil.relativedelta import relativedelta

class Dueño(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nombre

class Mascota(models.Model):
    OPCIONES_ESTERILIZADO = [
        (True, 'Sí'),
        (False, 'No')
    ]

    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    especie = models.CharField(max_length=50, verbose_name="Especie")
    raza = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Raza"
    )
    fecha_nacimiento = models.DateField(
        verbose_name="Fecha de Nacimiento",
        default='2023-01-01'
    )
    peso = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name="Peso (kg)"
    )
    esterilizado = models.BooleanField(
        default=False, verbose_name="Esterilizado"
    )
    dueño = models.ForeignKey(
        Dueño,
        on_delete=models.CASCADE,
        related_name='mascotas',
        verbose_name="Dueño"
    )

    def get_edad(self):
        """Calcula la edad en años y meses basada en la fecha de nacimiento"""
        if not self.fecha_nacimiento:
            return "Desconocida"
        
        hoy = date.today()
        diferencia = relativedelta(hoy, self.fecha_nacimiento)
        
        años = diferencia.years
        meses = diferencia.months
        
        if años == 0 and meses == 0:
            días = diferencia.days
            return f"{días} días"
        elif años == 0:
            return f"{meses} meses"
        elif meses == 0:
            return f"{años} año{'s' if años > 1 else ''}"
        else:
            return f"{años} año{'s' if años > 1 else ''} y {meses} mes{'es' if meses > 1 else ''}"

    def __str__(self):
        return f"{self.nombre} ({self.especie})"

class Visita(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='visitas')
    fecha = models.DateField()
    motivo = models.TextField(max_length=200)
    tratamiento = models.TextField(blank=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    # Estado de pago: pendiente / pago / cancelado
    ESTADOS_PAGO = [
        ("pendiente", "Pendiente de pago"),
        ("pago", "Pagado"),
        ("cancelado", "Cancelado"),
    ]
    estado = models.CharField(max_length=20, choices=ESTADOS_PAGO, default="pendiente", verbose_name="Estado de Pago")
    # Observaciones libres
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Visita de {self.mascota.nombre} el {self.fecha}"