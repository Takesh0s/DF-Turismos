from django.urls import path
from . import views

app_name = 'relatorios'

urlpatterns = [
    path('', views.painel_relatorios, name='painel'),
    path('turistas/', views.relatorio_turistas, name='turistas'),
    path('eventos/', views.relatorio_eventos, name='eventos'),
    path('exportar/turistas/', views.exportar_turistas, name='exportar_turistas'),
    path('exportar/eventos/', views.exportar_eventos, name='exportar_eventos'),
]