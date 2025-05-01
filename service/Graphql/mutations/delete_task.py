import graphene
from graphql import GraphQLError
from task.models import Task  

class DeleteTask(graphene.Mutation):
    success = graphene.Boolean()  

    class Arguments:
        tarea_id = graphene.Int(required=True) 

    def mutate(self, info, tarea_id):
        try:
            
            tarea = Task.objects.get(tarea_id=tarea_id)
            tarea.delete()  
            return DeleteTask(success=True)  
        except Task.DoesNotExist:
            raise GraphQLError(f"Tarea con id {tarea_id} no encontrada")  
