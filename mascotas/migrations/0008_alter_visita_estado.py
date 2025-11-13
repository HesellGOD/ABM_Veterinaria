# Generated migration to update Visita.estado choices to payment status

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0007_remove_mascota_edad_mascota_fecha_nacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visita',
            name='estado',
            field=models.CharField(
                choices=[
                    ('pendiente', 'Pendiente de pago'),
                    ('pago', 'Pagado'),
                    ('cancelado', 'Cancelado'),
                ],
                default='pendiente',
                max_length=20,
                verbose_name='Estado de Pago'
            ),
        ),
    ]
