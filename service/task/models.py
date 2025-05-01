from django.db import models

# Create your models here.

class Task(models.Model):

    class Estado(models.TextChoices):
        PENDIENTE = 'pendiente'
        EN_PROGRESO = 'en progreso'
        COMPLETADO = 'completado'

    tarea_id = models.AutoField(
        primary_key=True,
        db_column='tarea_id'
    )
    nombre = models.TextField()
    descripcion = models.TextField()
    estado = models.CharField(
        choices=Estado.choices,
        max_length=20
    )

    experto_cc = models.IntegerField()

    class Meta:
        db_table = 'tarea'
        managed = False 