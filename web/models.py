from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .gerenciador import Gerenciador

class UsuarioCustomizado(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("endereço de email", unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    endereco = models.CharField(max_length=200, null=True, blank=True)
    cpf = models.CharField(max_length=20, unique=True)  
    data_nascimento = models.DateField("data de nascimento")  
    
    objects = Gerenciador()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["cpf", "data_nascimento"]

    def __str__(self):
        return self.email


class CategoriaProdutos(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome


class Foto(models.Model):
    url = models.CharField(max_length=1000)

    def __str__(self):
        return self.url

class Produtos(models.Model):
    categoriaFK = models.ForeignKey(CategoriaProdutos, related_name='categoriaProdutos', on_delete=models.CASCADE)
    nome = models.CharField(max_length=150)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    quantidade = models.IntegerField()
    fotos = models.ManyToManyField(Foto)

    def __str__(self):
        return self.nome


STATUS_PAGAMENTOS = [
    ("P","PENDENTE"),
    ("A","APROVADO"),
    ("R","RECUSADO"),
    ("C","CANCELADO"),
]


class Vendas(models.Model):
    usuarioFK = models.ForeignKey(UsuarioCustomizado, related_name='usuarioVendas', on_delete=models.CASCADE)
    dataHora = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_PAGAMENTOS)

    def __str__(self):
            return self.status

class VendasProdutos(models.Model):
     produtoFK = models.ForeignKey(Produtos, related_name='vendasProdutos', on_delete=models.CASCADE)
     quantidade = models.IntegerField()
     vendaFK = models.ForeignKey(Vendas, related_name='vendasFK', on_delete=models.CASCADE)

     def __str__(self):
            return self.produtoFK.nome