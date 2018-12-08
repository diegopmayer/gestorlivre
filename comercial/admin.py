from django.contrib import admin
from .models import Produto
from .models import Pedido
from clientes.models import Categoria, Clientes

class ProdutoAdmin(admin.ModelAdmin):

    list_display = (
            'Produto_ativo',
            'Valor_de_custo',
            'Valor_de_venda',
            'Manual_tecnico_do_produto',
            'Imagem_do_produto',
            'Link_para_produto_no_site',
            'Obs_do_produto',
            'Data_de_cadastro_do_produto',)

    list_filter = (
            'Produto_ativo',
            'Valor_de_custo',
            'Valor_de_venda',
            'Manual_tecnico_do_produto',
            'Imagem_do_produto',
            'Link_para_produto_no_site',
            'Obs_do_produto',
            'Data_de_cadastro_do_produto',)

class PedidoAdmin(admin.ModelAdmin):

    list_display = (
            'Cliente_do_pedido',
            'Produto_pedido',
            'Metodo_de_entrega',
            'Data_prevista_para_entrega',
            'Data_de_cadastro_do_pedido',)

    list_filter = (
            'Cliente_do_pedido',
            'Produto_pedido',
            'Metodo_de_entrega',
            'Data_prevista_para_entrega',
            'Data_de_cadastro_do_pedido',)

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Pedido, PedidoAdmin)