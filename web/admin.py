from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

class AdminUsuarioCustomizado(UserAdmin):
    model = UsuarioCustomizado
    list_display = ['id', 'email', 'nome_completo', 'cpf', 'data_nascimento']
    list_display_links = ('id', 'email', 'nome_completo', 'cpf', 'data_nascimento',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('nome_completo', 'cpf', 'data_nascimento', 'telefone', 'endereco',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions',)}),
        ('Management', {'fields': ('last_login',)}),
    )
    filter_horizontal = ('groups', 'user_permissions',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'nome_completo', 'cpf', 'data_nascimento', 'is_staff', 'is_active', 'groups', 'user_permissions',),
        }),
    )
    search_fields = ['email', 'nome_completo', 'cpf']
    ordering = ['email']

admin.site.register(UsuarioCustomizado, AdminUsuarioCustomizado)

class AdminCategoria(admin.ModelAdmin):
    list_display = ['id', 'nome']
    list_display_links = ('id', 'nome',)
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(CategoriaProdutos,AdminCategoria)

class AdminFoto(admin.ModelAdmin):
    list_display = ['id','nome']
    list_display_links = ('id','nome',)
    search_fields = ('id',)
    list_per_page = 10
    
admin.site.register(Foto,AdminFoto)