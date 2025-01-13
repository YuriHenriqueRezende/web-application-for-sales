from django.contrib import admin
from .models import *


# Register your models here.
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'preco', 'estoque')  
    search_fields = ('id','nome',)  
    list_filter = ('preco',)
    list_per_page = 10  

admin.site.register(Produto,ProdutoAdmin)