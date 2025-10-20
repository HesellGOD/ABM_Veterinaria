from django.db import models

class Dueño(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50, blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    dueño = models.ForeignKey(Dueño, on_delete=models.CASCADE, related_name='mascotas')

    def __str__(self):
        return f"{self.nombre} ({self.especie})"

class Visita(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='visitas')
    fecha = models.DateField()
    motivo = models.TextField(max_length=200)
    tratamiento = models.TextField(blank=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"Visita de {self.mascota.nombre} el {self.fecha}"