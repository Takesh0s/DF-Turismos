from django.shortcuts import render
from django.http import HttpResponse
from turistas.models import Turista
from eventos.models import Evento
import csv

def painel_relatorios(request):
    return render(request, 'relatorios/painel.html')

def relatorio_turistas(request):
    turistas = Turista.objects.all()
    return render(request, 'relatorios/turistas.html', {'turistas': turistas})

def relatorio_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'relatorios/eventos.html', {'eventos': eventos})

def exportar_turistas(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="turistas.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['ID', 'Nome', 'Email', 'Telefone'])
    
    for turista in Turista.objects.all():
        writer.writerow([turista.id, turista.nome, turista.email, turista.telefone])
    
    return response

def exportar_eventos(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="eventos.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['ID', 'Nome', 'Data', 'Local'])
    
    for evento in Evento.objects.all():
        writer.writerow([evento.id, evento.nome, evento.data, evento.local])
    
    return response