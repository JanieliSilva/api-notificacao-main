from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from .models import Notificacao, NotificacaoEnvio
from .serializers import NotificacaoSerializer

Usuario = get_user_model()


class EmitirNotificacaoAPIView(APIView):
    """
    Endpoint que recebe os parâmetros da notificação e realiza o envio.
    """

    def post(self, request):
        serializer = NotificacaoSerializer(data=request.data)
        if serializer.is_valid():
            notificacao = serializer.save()

            # Define o público alvo
            if notificacao.notificacao_individual:
                destinatarios = Usuario.objects.filter(
                    email=request.data.get('email')
                )
            else:
                destinatarios = Usuario.objects.filter(
                    tipo_usuario=notificacao.grupo_de_envio
                )

            if not destinatarios.exists():
                return Response(
                    {"detail": "Nenhum destinatário encontrado."},
                    status=status.HTTP_404_NOT_FOUND
                )

            enviados = []
            for user in destinatarios:
                # Cria o registro de envio
                NotificacaoEnvio.objects.get_or_create(
                    template=notificacao,
                    usuario=user
                )

                # Envia o e-mail
                send_mail(
                    subject=notificacao.titulo,
                    message=notificacao.mensagem,
                    from_email='no-reply@sistema.com',
                    recipient_list=[user.email],
                    fail_silently=False,
                )
                enviados.append(user.email)

            return Response({
                "detail": f"Notificação enviada para {len(enviados)} usuário(s).",
                "emails": enviados
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

