import graphene
from .create_investigation import CreateInvestigation
from .update_investigation import UpdateInvestigation
from .delete_investigacion import DeleteInvestigation
from .delete_task import DeleteTask
from .update_task import UpdateTask
from .create_task import CreateTask
from .update_task_status import UpdateTaskStatus


class Mutation(graphene.ObjectType):

   create_investigation = CreateInvestigation.Field()
   create_task = CreateTask.Field()
   update_investigation = UpdateInvestigation.Field()
   update_task = UpdateTask.Field()
   delete_investigation = DeleteInvestigation.Field()
   delete_task = DeleteTask.Field()
   update_task_status = UpdateTaskStatus.Field()
