from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .gerenciador import Gerenciador

class UsuarioCustomizado(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("endereço de email", unique=True)
    nome_completo = models.CharField(max_length=150)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    endereco = models.CharField(max_length=200)
    cpf = models.CharField(max_length=20)
    data_nascimento = models.DateField()

    objects = Gerenciador()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['nome_completo', 'cpf', 'data_nascimento']

    def __str__(self):
        return self.email


class CategoriaProdutos(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome


class Foto(models.Model):
    nome = models.CharField(max_length=150)
    url = models.CharField(max_length=1000)

    def __str__(self):
        return self.nome

