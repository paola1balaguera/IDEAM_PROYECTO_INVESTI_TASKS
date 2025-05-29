from django.db import models
from investigation.models import Investigacion

# Create your models here.

class Task(models.Model):

    class Estado(models.TextChoices):
        PENDIENTE = 'pendiente'
        EN_PROGRESO = 'en progreso'
        COMPLETADO = 'completado'
        RETRASADO_POR_NOVEDAD = 'retrasado por novedad'

    tarea_id = models.AutoField(
        primary_key=True,
        db_column='tarea_id'
    )
    nombre = models.TextField()
    descripcion = models.TextField()
    estado = models.CharField(
        choices=Estado.choices,
        max_length=30
    )

    experto_cc = models.IntegerField()

    investigacion_id = models.ForeignKey(Investigacion, on_delete=models.CASCADE, db_column='investigacion_id')

    fecha_ejecucion = models.DateField()

    # retrasada_por_novedad = models.BooleanField()

    class Meta:
        db_table = 'tarea'
        managed = False 