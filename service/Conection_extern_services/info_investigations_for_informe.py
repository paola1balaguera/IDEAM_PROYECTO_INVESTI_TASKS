from django.http import JsonResponse
from Graphql.queries.queries import Query

def ejecutar_query_directa(request):
    id_investigacion = request.GET.get('id')

    try:
        information_about_investigation = Query.resolve_information_about_investigation(None, None, id_investigacion)

        information_about_tasks = Query.resolve_information_about_task_for_id_investigation(None, None, id_investigacion)

        print('hetttttttttttt')
       
        fecha_tareas_por_investi = Query.resolve_calculate_active_days(None, None, id_investigacion)


        tasks_serialized = [
            {
                "tarea_id": tarea.tarea_id,
                "estado": tarea.estado,
                'cedula_experto': tarea.experto_cc

                # agrega más campos si tienes
            }
            for tarea in information_about_tasks
        ]


        # print("miau",information_about_tasks.first())
        
        # for tarea in information_about_tasks:
        #     print(f"Tarea ID: {tarea.tarea_id}, Nombre: {tarea.nombre}, Estado: {tarea.estado}")

        
        if information_about_investigation is None:
            return JsonResponse({'error': 'Investigación no encontrada'}, status=404)

        fecha_inicio, fecha_fin, nombre = information_about_investigation

        return JsonResponse({
            "id": id_investigacion,
            "nombre": nombre,
            "fecha_inicio": fecha_inicio,
            "fecha_fin": fecha_fin,
            "tasks": tasks_serialized,
            'fechas_tareas_activas': fecha_tareas_por_investi
        }, status=200) 

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
