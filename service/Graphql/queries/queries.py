import graphene
from ..schemas.schema_investigation import InvestigationSchema
from ..schemas.schema_task import TaskSchema
from investigation.models import Investigacion
from task.models import Task
from django.db.models.functions import TruncDate



class Query(graphene.ObjectType):


    # -----------------------------------------

    all_investigations = graphene.List(InvestigationSchema)
    all_tasks = graphene.List(TaskSchema)
    investigacion_for_name = graphene.String(name=graphene.String(required=True))
    list_tasks_for_expert = graphene.List(TaskSchema, cc_experto=graphene.Int(required=True))
    information_about_investigation = graphene.Field(InvestigationSchema, id_investigation = graphene.Int(required=True))
    information_about_task_for_id_investigation = graphene.List(TaskSchema, id_investigation = graphene.Int(required=True))
    calculate_active_days = graphene.Field(TaskSchema,id_investigation=graphene.Int(required=True))

    


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
    
    def resolve_information_about_investigation(root, info, id_investigation):

        try:
            print("llego aqui chinga")
            investigacion = Investigacion.objects.get(investigacion_id=id_investigation)
            print(investigacion)
            return investigacion.fecha_inicio, investigacion.fecha_fin, investigacion.nombre
        
        except Investigacion.DoesNotExist:
            
            return None, None, None
        

    def resolve_information_about_task_for_id_investigation(root, info, id_investigation):

        try:
            tasks = Task.objects.filter(investigacion_id=id_investigation)

            print("eyyy:", tasks)

            return tasks
        except Task.DoesNotExist:

            return None
        

    def resolve_calculate_active_days(root, info, id_investigation):

        print('miauuu')
        
        tareas = Task.objects.filter(investigacion_id=id_investigation)

        print("dentro del resolve1")

        fechas = tareas.annotate(
            fecha_sin_hora=TruncDate("fecha_ejecucion")
        ).values_list("fecha_sin_hora", flat=True).distinct()

        print("dentro del resolve")

        fechas_str = [f.isoformat() for f in fechas if f is not None]

        return fechas_str