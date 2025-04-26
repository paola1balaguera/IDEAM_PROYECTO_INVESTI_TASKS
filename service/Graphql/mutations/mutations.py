import graphene
from .create_investigation import CreateInvestigation
from .update_investigation import UpdateInvestigation


class Mutation(graphene.ObjectType):

   create_investigation = CreateInvestigation.Field()
   update_investigation = UpdateInvestigation.Field()
