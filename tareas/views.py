from django.shortcuts import render, render_to_response
from django.http import HttpResponse

def crear_proyecto(request):
return render_to_response('crear_proyecto.html')

def crear_tarea(request):
return render_to_response('crear_tarea.html')

def historial_tareas(request):
return render_to_response('historial_tareas.html')

def proyectos_finalizados(request):
return render_to_response('proyectos_finalizados.html')

