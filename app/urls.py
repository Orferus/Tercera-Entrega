from django.conf.urls import patterns, include, url
from tareas.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^CrearTarea/$', crear_tarea),
    url(r'^CrearProyecto/$', crear_proyecto),
    url(r'^HistorialTareas/$', historial_tareas),
    url(r'^ProyectosFinalizados/$', proyectos_finalizados),
)