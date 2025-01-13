from django.contrib import admin
from .models import *


# Register your models here.
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id','nome')  
    search_fields = ('id','nome',)  
    list_filter = ('nome',)
    list_per_page = 10  

admin.site.register(Produto,ProdutoAdmin)