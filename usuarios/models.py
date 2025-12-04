from django.db import models
from django.contrib.auth.models import AbstractUser

TIPO_USUARIO = [
    ('1', 'Cliente'),
    ('2', 'Funcionario'),
    ('3', 'Administrador'),
]


class Usuario(AbstractUser):

    tipo_usuario = models.CharField(max_length=1,
                                    choices=TIPO_USUARIO,
                                    default='1',
                                    verbose_name='Tipo de Usuário'
                                    )

    def __str__(self):
        return self.username + '-' + self.email
