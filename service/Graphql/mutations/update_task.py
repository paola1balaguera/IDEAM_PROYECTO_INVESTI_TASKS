import graphene
from graphene_django.types import DjangoObjectType
from ..schemas.schema_task import TaskSchema
from task.models import Task
from Graphql.queries.queries import Query


class UpdateTask(graphene.Mutation):
    class Arguments:
        tarea_id = graphene.Int(required=True)  
        nombre = graphene.String(required=False)
        descripcion = graphene.String(required=False)
        estado = graphene.String(required=False)
        experto_cc = graphene.Int(required=False)

    task = graphene.Field(TaskSchema)

    def mutate(self, info, tarea_id, nombre=None, descripcion=None, estado=None, experto_cc=None):
        try:

            # id = Query.resolve_task_for_name(None, None, nombre)

            # Buscar la tarea por su tarea_id
            tarea = Task.objects.get(tarea_id=tarea_id)

            # Actualizar los campos solo si se pasan valores
            if nombre:
                tarea.nombre = nombre
            if descripcion:
                tarea.descripcion = descripcion
            if estado:
                tarea.estado = estado
            if experto_cc is not None:
                tarea.experto_cc = experto_cc

            # Guardar los cambios
            tarea.save()

            return UpdateTask(task=tarea)
        except Task.DoesNotExist:
            raise Exception("Tarea no encontrada") 