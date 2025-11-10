from django.db import models

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
    raza = models.CharField(max_length=50, blank=True, null=True, verbose_name="Raza")
    edad = models.IntegerField(verbose_name="Edad (años)")
    peso = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Peso (kg)")
    esterilizado = models.BooleanField(default=False, verbose_name="Esterilizado")
    dueño = models.ForeignKey(Dueño, on_delete=models.CASCADE, related_name='mascotas', verbose_name="Dueño")

    def __str__(self):
        return f"{self.nombre} ({self.especie})"

class Visita(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='visitas')
    fecha = models.DateField()
    motivo = models.TextField(max_length=200)
    tratamiento = models.TextField(blank=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    # Nuevo campo estado (pendiente / confirmada / completada)
    ESTADOS = [
        ("pendiente", "Pendiente"),
        ("confirmada", "Confirmada"),
        ("completada", "Completada"),
    ]
    estado = models.CharField(max_length=20, choices=ESTADOS, default="pendiente")
    # Observaciones libres
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Visita de {self.mascota.nombre} el {self.fecha}"