import graphene
from ..schemas.schema_investigation import InvestigationSchema
from investigation.models import Investigacion



class Query(graphene.ObjectType):


    # -----------------------------------------

    all_investigations = graphene.List(InvestigationSchema)

    


    def resolve_all_investigations(root, info):

        return Investigacion.objects.all()
    
 