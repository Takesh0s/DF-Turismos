from django.shortcuts import render

from django.shortcuts import render
from .models import Parque

def lista_parques(request):
    parques = Parque.objects.all()
    return render(request, 'parques/lista.html', {'parques': parques})

