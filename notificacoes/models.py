from django.db import models
from django.contrib.auth import get_user_model
from usuarios.models import TIPO_USUARIO

Usuario_API = get_user_model()

TIPO_N_CHOICES = [
    ('INFO', 'Informativa'),
    ('ALERT', 'Alerta'),
    ('PROMOCAO', 'Promoção'),
]


class Notificacao(models.Model):
    """
    Define o conteúdo base da notificação e quem deve recebê-la.
    Este modelo não registra o envio, apenas a intenção e o conteúdo.
    """

    titulo = models.CharField(max_length=100, blank=False)

    mensagem = models.TextField(blank=False)

    lida = models.BooleanField(default=False)

    tipo_notificacao = models.CharField(
        max_length=10, choices=TIPO_N_CHOICES, default='INFO')

    grupo_de_envio = models.CharField(max_length=1,
                                      choices=TIPO_USUARIO,
                                      default='1',
                                      verbose_name='Tipo de Usuário'
                                      )

    notificacao_individual = models.BooleanField(
        default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    ativa = models.BooleanField(
        default=True, help_text='Se a notificação pode ser enviada.')

    class Meta:
        ordering = ['-data_criacao']



class NotificacaoEnvio(models.Model):
    """
    Registra que uma notificação foi enviada a um usuário específico.
    É o registro que o usuário irá ver em sua caixa de entrada.
    """

    template = models.ForeignKey(
        Notificacao,
        on_delete=models.CASCADE,
        related_name='envios'
    )

    # Liga ao usuário que recebeu
    usuario = models.ForeignKey(
        Usuario_API,
        on_delete=models.CASCADE,
        related_name='notificacoes_recebidas'
    )

    # Status de leitura
    lida = models.BooleanField(default=False)

    # Data de registro do envio
    data_envio = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Garante que as mais recentes apareçam primeiro
        ordering = ['-data_envio']
        # Garante que um usuário não receba a mesma notificação template duas vezes
        unique_together = ('template', 'usuario')
