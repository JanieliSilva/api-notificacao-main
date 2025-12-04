from django.urls import path
from .views import EmitirNotificacaoAPIView

urlpatterns = [
    path('emitir/', EmitirNotificacaoAPIView.as_view(), name='emitir-notificacao'),
]