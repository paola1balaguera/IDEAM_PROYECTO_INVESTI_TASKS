import graphene
from ..schemas.schema_investigation import InvestigationSchema
from investigation.models import Investigacion
from graphql import GraphQLError

class UpdateInvestigation(graphene.Mutation):
    investigacion = graphene.Field(InvestigationSchema)

    class Arguments:
        id = graphene.ID(required=True)
        fecha_inicio = graphene.types.datetime.Date()
        fecha_fin = graphene.types.datetime.Date()
        coordenadas_geograficas = graphene.String()

    def mutate(self, info, id, fecha_inicio=None, fecha_fin=None, coordenadas_geograficas=None):
        try:
            inv = Investigacion.objects.get(pk=id)
        except Investigacion.DoesNotExist:
            raise GraphQLError(f"Investigación con id={id} no encontrada")

        # Actualizamos sólo los campos que llegaron en la petición
        if fecha_inicio is not None:
            inv.fecha_inicio = fecha_inicio
        if fecha_fin is not None:
            inv.fecha_fin = fecha_fin
        if coordenadas_geograficas is not None:
            inv.coordenadas_geograficas = coordenadas_geograficas

        inv.save()
        return UpdateInvestigation(investigacion=inv)