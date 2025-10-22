from django import forms
from .models import Dueño, Mascota, Visita

class DueñoForm(forms.ModelForm):
    class Meta:
        model = Dueño
        fields = '__all__'


class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = '__all__'


class VisitaForm(forms.ModelForm):
    class Meta:
        model = Visita
        fields = '__all__'
