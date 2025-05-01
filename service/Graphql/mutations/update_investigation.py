import graphene
from graphql import GraphQLError
from ..schemas.schema_investigation import InvestigationSchema
from investigation.models import Investigacion

class UpdateInvestigation(graphene.Mutation):
    investigacion = graphene.Field(InvestigationSchema)

    class Arguments:
        investigacion_id = graphene.Int(required=True)  
        nombre = graphene.String(required=False)
        fecha_inicio = graphene.types.datetime.Date(required=False)
        fecha_fin = graphene.types.datetime.Date(required=False)
        coordenadas_geograficas = graphene.String(required=False)

    def mutate(self, info, investigacion_id, nombre=None, fecha_inicio=None, fecha_fin=None, coordenadas_geograficas=None):
        try:

            inv = Investigacion.objects.get(investigacion_id=investigacion_id)
        except Investigacion.DoesNotExist:
            raise GraphQLError(f"Investigación con id {investigacion_id} no encontrada")


        if nombre is not None:
            inv.nombre = nombre
        if fecha_inicio is not None:
            inv.fecha_inicio = fecha_inicio
        if fecha_fin is not None:
            inv.fecha_fin = fecha_fin
        if coordenadas_geograficas is not None:
            inv.coordenadas_geograficas = coordenadas_geograficas


        inv.save()

        return UpdateInvestigation(investigacion=inv)
