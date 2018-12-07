from django.contrib import admin
from .models import Clientes, Categoria

class CategoriaAdmin(admin.ModelAdmin):
    list_display = (
        'Nome_da_categoria',
        'Ativada',
        'Obs_da_categoria',
        'Data_de_cadastro_da_categoria',
    )
    list_filter = (
        'Nome_da_categoria',
        'Ativada',
        'Obs_da_categoria',
        'Data_de_cadastro_da_categoria',
    )
class clientesAdmin(admin.ModelAdmin):
    list_display = (
        'Categoria_do_cliente',
        'Cliente_ativo',
        'Nome_fantasia',
        'Nome_do_cliente',
        'Razao_social',
        'Logo_do_cliente',
        'Telefone_1',
        'Telefone_2',
        'Celular_1',
        'Site_do_cliente',
        'Tipo_juridico_do_cliente',
        'Cnpj',
        'Inscricao_estadual',
        'Possui_contrato',
        'Contrato_ou_proposta_anexado',
        'Valor_total_do_contrato',
        'CEP',
        'Cidade',
        'Estado',
        'Email_do_cliente',
        'Obs_do_cliente',
        'Data_de_cadastro_do_cliente',
    )
    list_filter = (
        'Categoria_do_cliente',
        'Cliente_ativo',
        'Nome_fantasia',
        'Nome_do_cliente',
        'Razao_social',
        'Logo_do_cliente',
        'Telefone_1',
        'Telefone_2',
        'Celular_1',
        'Site_do_cliente',
        'Tipo_juridico_do_cliente',
        'Cnpj',
        'Inscricao_estadual',
        'Possui_contrato',
        'Contrato_ou_proposta_anexado',
        'Valor_total_do_contrato',
        'CEP',
        'Cidade',
        'Estado',
        'Email_do_cliente',
        'Obs_do_cliente',
        'Data_de_cadastro_do_cliente',
    )
admin.site.register(Clientes, clientesAdmin)
admin.site.register(Categoria, CategoriaAdmin)