import graphene
from graphene_django import DjangoObjectType
from investigation.models import Investigacion


class InvestigationSchema(DjangoObjectType):
    class Meta:
        model = Investigacion
        fields = ("investigacion_id","nombre", "fecha_inicio", "fecha_fin", "coordenadas_geograficas")