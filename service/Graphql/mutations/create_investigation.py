import graphene
from ..schemas.schema_investigation import InvestigationSchema
from investigation.models import Investigacion
from ..queries.queries import Query


class CreateInvestigation(graphene.Mutation):
    investigacion = graphene.Field(InvestigationSchema)

    class Arguments:
        fecha_inicio = graphene.types.datetime.Date(required=True)
        fecha_fin = graphene.types.datetime.Date(required=True)
        coordenadas_geograficas = graphene.String(required=True)

    def mutate(self, info, fecha_inicio, fecha_fin, coordenadas_geograficas):
        inv = Investigacion.objects.create(
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            coordenadas_geograficas=coordenadas_geograficas
        )
        return CreateInvestigation(investigacion=inv)