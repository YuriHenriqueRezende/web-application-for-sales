from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UsuarioCustomizado, Guarda, UsuarioGuarda, Troca, TrocaAtirador, TrocaGuarda, Notificacao

class UsuarioCustomizadoAdmin(UserAdmin):
    model = UsuarioCustomizado
    list_display = ('email', 'nome_completo', 'cpf', 'tipo', 'sexo', 'numero_atirador', 'is_active', 'is_staff')
    search_fields = ('email', 'nome_completo', 'cpf', 'numero_atirador')
    list_filter = ('tipo', 'sexo', 'is_active', 'is_staff')
    ordering = ('email',)
    fieldsets = (
        ("Informações Pessoais", {'fields': ('email', 'nome_completo', 'cpf', 'data_nascimento', 'sexo', 'telefone', 'endereco')}),
        ("Informações Militares", {'fields': ('tipo', 'numero_atirador', 'ano_turma', 'trabalho', 'escolaridade', 'ra', 'mae', 'pai', 'tipo_sanguineo')}),
        ("Permissões", {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nome_completo', 'cpf', 'data_nascimento', 'sexo', 'password1', 'password2', 'is_active', 'is_staff')
        }),
    )

admin.site.register(UsuarioCustomizado, UsuarioCustomizadoAdmin)

class GuardaAdmin(admin.ModelAdmin):
    list_display = ('id', 'data_inicio', 'data_fim', 'turno')
    list_filter = ('turno',)
    search_fields = ('data_inicio', 'data_fim')
    ordering = ('data_inicio',)

admin.site.register(Guarda, GuardaAdmin)

class UsuarioGuardaAdmin(admin.ModelAdmin):
    list_display = ('id_guarda', 'numero_atirador')
    search_fields = ('numero_atirador__numero_atirador',)
    ordering = ('id_guarda',)

admin.site.register(UsuarioGuarda, UsuarioGuardaAdmin)

class TrocaAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'data_solicitada', 'ultima_modificacao')
    list_filter = ('status',)
    search_fields = ('id', 'status')
    ordering = ('-data_solicitada',)

admin.site.register(Troca, TrocaAdmin)

class TrocaAtiradorAdmin(admin.ModelAdmin):
    list_display = ('id_troca', 'numero_atirador', 'tipo')
    list_filter = ('tipo',)
    search_fields = ('numero_atirador__numero_atirador', 'id_troca')
    ordering = ('id_troca',)

admin.site.register(TrocaAtirador, TrocaAtiradorAdmin)

class TrocaGuardaAdmin(admin.ModelAdmin):
    list_display = ('id_troca', 'id_guarda')
    search_fields = ('id_troca', 'id_guarda')
    ordering = ('id_troca',)

admin.site.register(TrocaGuarda, TrocaGuardaAdmin)

class NotificacaoAdmin(admin.ModelAdmin):
    list_display = ('numero_atirador', 'data_envio', 'status')
    list_filter = ('status',)
    search_fields = ('numero_atirador__numero_atirador', 'mensagem')
    ordering = ('-data_envio',)

admin.site.register(Notificacao, NotificacaoAdmin)
