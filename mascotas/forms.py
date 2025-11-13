from django import forms
from .models import Dueño, Mascota, Visita

class DueñoForm(forms.ModelForm):
    class Meta:
        model = Dueño
        fields = '__all__'


class MascotaForm(forms.ModelForm):
    # Aseguramos que la fecha use formato ISO para que el widget type="date" muestre el valor al editar
    fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d', attrs={
            'class': 'form-control rounded-3 py-2',
            'type': 'date'
        }),
        input_formats=['%Y-%m-%d'],
        label='Fecha de Nacimiento'
    )

    class Meta:
        model = Mascota
        fields = ['nombre', 'especie', 'raza', 'fecha_nacimiento', 'peso', 'esterilizado', 'dueño']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control rounded-3 py-2',
                'placeholder': 'Ej: Luna'
            }),
            'especie': forms.TextInput(attrs={
                'class': 'form-control rounded-3 py-2',
                'placeholder': 'Ej: Perro/Gato'
            }),
            'raza': forms.TextInput(attrs={
                'class': 'form-control rounded-3 py-2',
                'placeholder': 'Ej: Labrador'
            }),
            'peso': forms.NumberInput(attrs={
                'class': 'form-control rounded-3 py-2',
                'placeholder': 'Ej: 15.5',
                'step': '0.1'
            }),
            'esterilizado': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'dueño': forms.Select(attrs={
                'class': 'form-select rounded-3 py-2'
            })
        }


class VisitaForm(forms.ModelForm):
    # Aseguramos que la fecha use formato ISO para que el widget type="date" muestre el valor al editar
    fecha = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d', attrs={
            'class': 'form-control rounded-3 py-2',
            'type': 'date'
        }),
        input_formats=['%Y-%m-%d']
    )

    class Meta:
        model = Visita
        fields = ['mascota', 'fecha', 'motivo', 'tratamiento', 'peso', 'estado', 'observaciones']
        widgets = {
            'mascota': forms.Select(attrs={
                'class': 'form-select rounded-3 py-2',
                'placeholder': 'Seleccione una mascota'
            }),
            'motivo': forms.TextInput(attrs={
                'class': 'form-control rounded-3 py-2',
                'placeholder': 'Describa el motivo de la visita'
            }),
            'tratamiento': forms.TextInput(attrs={
                'class': 'form-control rounded-3 py-2',
                'placeholder': 'Describa el tratamiento aplicado'
            }),
            'peso': forms.NumberInput(attrs={
                'class': 'form-control rounded-3 py-2',
                'placeholder': 'Ej: 15.5',
                'step': '0.1'
            }),
            'estado': forms.Select(attrs={
                'class': 'form-select rounded-3 py-2'
            }),
            'observaciones': forms.Textarea(attrs={
                'class': 'form-control rounded-3',
                'rows': 3,
                'placeholder': 'Observaciones adicionales'
            })
        }
