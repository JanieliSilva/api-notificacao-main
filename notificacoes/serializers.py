from rest_framework import serializers
from .models import Notificacao

class NotificacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacao
        fields = [
            'id', 'titulo', 'mensagem', 'tipo_notificacao',
            'grupo_de_envio', 'notificacao_individual', 'ativa'
        ]
