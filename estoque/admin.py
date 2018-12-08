from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'Nome_do_item',
        'Valor_pago',
        'Nota_fiscal_do_item',
        'Imagem_do_item',
        'Obs_do_item',
        'Data_de_cadastro_do_item',)
    list_filter = (
        'Nome_do_item',
        'Valor_pago',
        'Nota_fiscal_item',
        'Imagem_do_item',
        'Obs_do_item',
        'Data_de_cadastro_do_item',)

admin.site.register(Item, ItemAdmin)