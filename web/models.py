from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .gerenciador import Gerenciador

SEXO_CHOICES = [('M', 'Masculino'), ('F', 'Feminino')]
TIPO_CHOICES = [('SB', 'Subtenente'), ('A', 'Atirador'), ('S', 'Sargento'), ('C', 'Cabo')]
class UsuarioCustomizado(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("endereço de email", unique=True)
    nome_completo = models.CharField(max_length=150)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    endereco = models.CharField(max_length=200)
    cpf = models.CharField(max_length=20, unique=True)
    data_nascimento = models.DateField()
    ano_turma = models.IntegerField(null=True, blank=True)
    tipo = models.CharField(max_length=2, choices=TIPO_CHOICES)
    trabalho = models.CharField(max_length=50, null=True, blank=True)
    escolaridade = models.CharField(max_length=50, null=True, blank=True)
    ra = models.CharField(max_length=20, null=True, blank=True)
    mae = models.CharField(max_length=100, null=True, blank=True)
    pai = models.CharField(max_length=100, null=True, blank=True)
    tipo_sanguineo = models.CharField(max_length=3, null=True, blank=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    numero_atirador = models.IntegerField(unique=True, null=True, blank=True)

    objects = Gerenciador()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['nome_completo', 'cpf', 'data_nascimento']

    def __str__(self):
        return str(self.numero_atirador) if self.numero_atirador is not None else self.email

class Guarda(models.Model):
    TURNO_CHOICES = [('Manhã', 'Manhã'), ('Tarde', 'Tarde'), ('Noite', 'Noite')]
    
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    turno = models.CharField(max_length=10, choices=TURNO_CHOICES)
    
    def __str__(self):
        return f"Guarda {self.id} - {self.data_inicio.strftime('%d/%m/%Y')}"

class UsuarioGuarda(models.Model):
    id_guarda = models.ForeignKey(Guarda, on_delete=models.CASCADE)
    numero_atirador = models.ForeignKey(UsuarioCustomizado, to_field='numero_atirador', on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return f"{self.numero_atirador} na Guarda {self.id_guarda}"

class Troca(models.Model):
    STATUS_CHOICES = [('Pendente', 'Pendente'), ('Aprovada', 'Aprovada'), ('Rejeitada', 'Rejeitada')]
    
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pendente')
    data_solicitada = models.DateTimeField(auto_now_add=True)
    motivo = models.TextField(null=True, blank=True)
    ultima_modificacao = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Troca {self.id} - {self.status}"

class TrocaAtirador(models.Model):
    TIPO_CHOICES = [('Solicitante', 'Solicitante'), ('Substituto', 'Substituto')]
    
    id_troca = models.ForeignKey(Troca, on_delete=models.CASCADE)
    numero_atirador = models.ForeignKey(UsuarioCustomizado, to_field='numero_atirador', on_delete=models.CASCADE, null=False)
    tipo = models.CharField(max_length=12, choices=TIPO_CHOICES)
    
    def __str__(self):
        return f"{self.tipo} - {self.numero_atirador} na Troca {self.id_troca}"

class TrocaGuarda(models.Model):
    id_guarda = models.ForeignKey(Guarda, on_delete=models.CASCADE)
    id_troca = models.ForeignKey(Troca, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Troca {self.id_troca} - Guarda {self.id_guarda}"
    
class Notificacao(models.Model):
    STATUS_CHOICES = [('Enviada', 'Enviada'), ('Lida', 'Lida'), ('Pendente', 'Pendente')]
    
    numero_atirador = models.ForeignKey(UsuarioCustomizado, to_field='numero_atirador', on_delete=models.CASCADE, null=False)
    data_envio = models.DateTimeField(auto_now_add=True)
    mensagem = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pendente')
    
    def __str__(self):
        return f"Notificação para {self.numero_atirador} - {self.status}"
