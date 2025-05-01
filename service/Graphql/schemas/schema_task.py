import graphene
from graphene_django import DjangoObjectType
from task.models import Task


class TaskSchema(DjangoObjectType):
    class Meta:
        model = Task
