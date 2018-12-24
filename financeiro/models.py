from django.db import models
from clientes.models import Categoria, Clientes
from fornecedores.models import Fornecedor
from django.conf import settings

class Conta_bancaria(models.Model):
    Dono_da_conta = models.CharField(
            max_length=100,
            null=True,
            blank=True)
    def __str__(self):
        return self.Dono_da_conta
    BANCO = (
            ("BB", "Banco do Brasil"),
            ("CX", "Caixa Econômica"),
            ("BR", "Bradesco"),
            )
    Banco_da_conta = models.CharField(
            max_length=100,
            choices=BANCO,
            null=True,
            blank=True)
    Agencia = models.CharField(
            max_length=100)
    Conta = models.CharField(
            max_length=100)
    Operacao = models.CharField(
            max_length=100)
class Categoria_registro(models.Model):
    Nome_da_categoria = models.CharField(
            max_length=100,
            null=True,
            blank=True)
    def __str__(self):
        return self.Nome_da_categoria
    Ativada = models.BooleanField()

    Obs_da_categoria = models.TextField(
            null=True,
            blank=True)
    Data_de_cadastro_da_categoria = models.CharField(
            max_length=100,
            null=True,
            blank=True)
class Registro_financeiro(models.Model):
    STATUS = (
            ("AB", "Aberto"),
            ("FE", "Fechado"),
            ("PE", "Pendente")
            )
    Status_do_registro = models.CharField(
            max_length=100,
            choices=STATUS,
            null=True,
            blank=True)
    Categoria_do_registro = models.ForeignKey(
            Categoria_registro,
            on_delete=models.CASCADE,
            null=True,
            blank=True)
    Cliente_do_registro = models.ForeignKey(
            Clientes,
            on_delete=models.CASCADE,
            null=True,
            blank=True)
    Fornecedor_do_registro = models.ForeignKey(
            Fornecedor,
            on_delete=models.CASCADE,
            null=True,
            blank=True)
    Pagamento_para_colaborador = models.OneToOneField(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
            null=True,
            blank=True)
    Produto_do_registro = models.CharField(
            max_length=100,
            null=True,
            blank=True)
    TIPO = (
            ("EN", "Entrada"),
            ("SD", "Saída"),
            )
    Tipo_do_registro = models.CharField(
            choices=TIPO,
            max_length=100,
            null=True,
            blank=True)
    FORMA = (
            ("BO", "Boleto"),
            ("NP", "Nota Promissória"),
            ("TR", "Tranferência bancária"),
            ("CH", "Cheque"),
            ("CT", "Cartão de Crédito"),
            ("ES", "Espéciemax_length=100"),
            )
    Conta_de_saida = models.ForeignKey(
            Conta_bancaria,
            on_delete=models.CASCADE,
            related_name='Entrada',
            null=True,
            blank=True)
    Conta_de_entrada = models.ForeignKey(
            Conta_bancaria,
            on_delete=models.CASCADE,
            related_name='Entrada',
            null=True,
            blank=True)
    Forma_do_registro = models.CharField(
            max_length=100,
            choices=FORMA,
            null=True,
            blank=True)
    Valor_do_registro = models.FloatField()

    Valor_pago_em_imposto = models.FloatField()

    Vencimento = models.DateField(
            null=True,
            blank=True)
    Pago = models.BooleanField()

    Nota_fiscal_do_registro = models.FileField(upload_to='upload/',
            null=True,
            blank=True)
    Obs_do_registro = models.TextField(
            null=True,
            blank=True)
    Data_do_registro = models.DateField(
            null=True,
            blank=True)