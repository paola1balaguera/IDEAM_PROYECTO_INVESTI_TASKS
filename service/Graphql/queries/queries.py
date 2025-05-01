import graphene
from ..schemas.schema_investigation import InvestigationSchema
from ..schemas.schema_task import TaskSchema
from investigation.models import Investigacion
from task.models import Task



class Query(graphene.ObjectType):


    # -----------------------------------------

    all_investigations = graphene.List(InvestigationSchema)
    investigacion_for_name = graphene.String(name=graphene.String(required=True))
    list_tasks_for_expert = graphene.List(TaskSchema, cc_experto=graphene.Int(required=True))
    


    


    def resolve_all_investigations(root, info):

        return Investigacion.objects.all()
    
    def resolve_investigacion_for_name(root, info, name):

        investigacion = Investigacion.objects.filter(nombre = name).first()

        if investigacion:
            return investigacion.investigacion_id
        
        return None
    
    def resolve_all_tasks(root, info):
        return Task.objects.all()
    

    def resolve_task_for_name(root, info, name):

        task = Task.objects.filter(nombre = name).first()

        if task:
            return task.id
        
        return None
    
    def resolve_list_tasks_for_expert(root, info, cc_experto):

        experto = Task.objects.filter(experto_cc = cc_experto)

        if experto:
            return experto
        
        return None
 