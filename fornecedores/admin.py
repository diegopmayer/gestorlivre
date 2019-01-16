from django.contrib import admin
from .models import Fornecedor

class FornecedorAdmin(admin.ModelAdmin):
   
    list_display = (
        'Usuario_responsavel',
        'Nome_do_fornecedor',
        'Principal_item_fornecedor',
        'Fornecedor_ativo',
        'Logo_do_fornecedor',
        'Data_de_fundacao_do_fornecedor',
        'Abre',
        'Fecha',
        'Site_do_fornecedor',
        'Email_do_fornecedor',
        'Telefone_1',
        'Telefone_2',
        'Celular_direto_do_proprietario',
        'Contrato_do_fornecedor',
        'Ultima_reuniao_de_alinhamento',
        'Usuario_representante_na_ultima_reuniao',
        'Obs_do_fornecedor',
        'Data_de_cadastro_do_fornecedor')
    list_filter = (
        'Usuario_responsavel',
        'Nome_do_fornecedor',
        'Principal_item_fornecedor',
        'Fornecedor_ativo',
        'Logo_do_fornecedor',
        'Data_de_fundacao_do_fornecedor',
        'Abre',
        'Fecha',
        'Site_do_fornecedor',
        'Email_do_fornecedor',
        'Telefone_1',
        'Telefone_2',
        'Celular_direto_do_proprietario',
        'Contrato_do_fornecedor',
        'Ultima_reuniao_de_alinhamento',
        'Usuario_representante_na_ultima_reuniao',
        'Obs_do_fornecedor',
        'Data_de_cadastro_do_fornecedor')

admin.site.register(Fornecedor, FornecedorAdmin)