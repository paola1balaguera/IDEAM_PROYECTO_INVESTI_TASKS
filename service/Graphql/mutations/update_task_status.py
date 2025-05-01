import graphene
from graphql import GraphQLError
from task.models import Task  
from ..schemas.schema_task import TaskSchema  
class UpdateTaskStatus(graphene.Mutation):
    task = graphene.Field(TaskSchema)

    class Arguments:
        tarea_id = graphene.Int(required=True)  
        estado = graphene.String(required=True) 

    def mutate(self, info, tarea_id, estado):
        try:
          
            tarea = Task.objects.get(tarea_id=tarea_id)

          
            tarea.estado = estado


            tarea.save()

            return UpdateTaskStatus(task=tarea)
        except Task.DoesNotExist:
            raise GraphQLError(f"Tarea con id {tarea_id} no encontrada")  