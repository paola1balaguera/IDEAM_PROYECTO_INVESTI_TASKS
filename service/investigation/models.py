from django.db import models

# Create your models here.

class Investigacion(models.Model):
    investigacion_id = models.AutoField(
        primary_key=True,
        db_column='investigacion_id'
    )
    nombre = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    coordenadas_geograficas = models.CharField(max_length=255)

    class Meta:
        db_table = 'investigacion'
        managed = False 

