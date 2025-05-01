import graphene
from graphene_django.types import DjangoObjectType
from ..schemas.schema_task import TaskSchema
from task.models import Task

class CreateTask(graphene.Mutation):
    class Arguments:
        nombre = graphene.String(required=True)
        descripcion = graphene.String(required=True)
        estado = graphene.String(required=True)
        experto_cc = graphene.Int(required=True)

    task = graphene.Field(TaskSchema)

    def mutate(self, info, nombre, descripcion, estado, experto_cc):
       
        tarea = Task.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            estado=estado,
            experto_cc=experto_cc
        )
        return CreateTask(task=tarea)
