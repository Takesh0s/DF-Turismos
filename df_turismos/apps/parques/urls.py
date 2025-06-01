from django.urls import path
from . import views

app_name = 'parques'

urlpatterns = [
    path('', views.lista_parques, name='lista'),
]
