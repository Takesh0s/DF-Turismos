from django.db import models
from django.contrib.auth import get_user_model
from eventos.models import Evento

Usuario = get_user_model()

class Relatorio(models.Model):
    TIPOS_RELATORIO = [
        ('TUR', 'Turistas'),
        ('EVE', 'Eventos'),
        ('FIN', 'Financeiro'),
    ]

    tipo = models.CharField(max_length=3, choices=TIPOS_RELATORIO)
    parametros = models.JSONField()
    criado_por = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    arquivo = models.FileField(upload_to='relatorios/', null=True, blank=True)

    class Meta:
        verbose_name = 'Relatório'
        verbose_name_plural = 'Relatórios'
        ordering = ['-criado_em']

    def __str__(self):
        return f"Relatório de {self.get_tipo_display()} - {self.criado_em.strftime('%d/%m/%Y')}"
