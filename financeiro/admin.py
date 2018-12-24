from django.contrib import admin
from .models import Conta_bancaria, Categoria_registro, Registro_financeiro

class Conta_bancariaAdmin(admin.ModelAdmin):
    list_display = (
        'Dono_da_conta',
        'Banco_da_conta',
        'Agencia',
        'Conta',
        'Operacao',
        )
    list_filter = (
        'Dono_da_conta',
        'Banco_da_conta',
        'Agencia',
        'Conta',
        'Operacao',
        )

class Categoria_registroAdmin(admin.ModelAdmin):
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

class Registro_financeiroAdmin(admin.ModelAdmin):
    list_display = (
        'Status_do_registro',
        'Categoria_do_registro',
        'Cliente_do_registro',
        'Fornecedor_do_registro',
        'pagamento_para_colaborador',
        'Produto_do_registro',
        'Tipo_de_registro',
        'Conta_de_saida',
        'Conta_de_entrada',
        'Forma_do_registro',
        'Valor_do_registro',
        'Valor_pago_em_impostos',
        'Vencimento',
        'Pago',
        'Nota_fiscal_do_registro',
        'Obs_do_registro',
        'Data_do_registro',
        )
    list_filter = (
        'Status_do_registro',
        'Categoria_do_registro',
        'Cliente_do_registro',
        'Fornecedor_do_registro',
        'pagamento_para_colaborador',
        'Produto_do_registro',
        'Tipo_de_registro',
        'Conta_de_saida',
        'Conta_de_entrada',
        'Forma_do_registro',
        'Valor_do_registro',
        'Valor_pago_em_impostos',
        'Vencimento',
        'Pago',
        'Nota_fiscal_do_registro',
        'Obs_do_registro',
        'Data_do_registro',
        )

admin.site.register(Conta_bancaria, Conta_bancariaAdmin)
admin.site.register(Categoria_registro, Categoria_registroAdmin)
admin.site.register(Registro_financeiro, Registro_financeiroAdmin)
