import graphene
from graphql import GraphQLError
from investigation.models import Investigacion

class DeleteInvestigation(graphene.Mutation):
    success = graphene.Boolean()  
    class Arguments:
        id = graphene.Int(required=True)  

    def mutate(self, info, id):
        try:
            
            inv = Investigacion.objects.get(investigacion_id=id)
            inv.delete()  
            return DeleteInvestigation(success=True)  
        except Investigacion.DoesNotExist:
            raise GraphQLError(f"Investigación con id {id} no encontrada")  # Si no se encuentra la investigación, lanzamos un error
