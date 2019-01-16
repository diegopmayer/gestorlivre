from django.db import models
from estoque.models import Item
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField

class Fornecedor(models.Model):

    Usuario_responsavel = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='Responsavel',
        on_delete=models.CASCADE)
    Nome_do_fornecedor = models.CharField(
        max_length=100,
        null=True,
        blank=True)
    def __str__(self):
        return self.Nome_do_Fornecedor
    
    Principal_item_fornecedor = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        null=True,
        blank=True)
    
    Fornecedor_ativo = models.BooleanField()

    Logo_do_fornecedor = models.ImageField(
        upload_to='upload/',
        null=True,
        blank=True)
    Data_de_fundacao_do_fornecedor = models.DateField(
        null=True,
        blank=True)
    Abre = models.TimeField(
        null=True,
        blank=True)
    Fecha = models.TimeField(
        null=True,
        blank=True)
    Site_do_fornecedor = models.URLField(
        null=True,
        blank=True)
    Email_do_fornecedor = models.EmailField(
        null=True,
        blank=True)
    Telefone_1 = PhoneNumberField()

    Telefone_2 = PhoneNumberField()

    Celular_direto_do_proprietario = PhoneNumberField()

    Contrato_do_fornecedor = models.FileField(
        upload_to='upload/',
        null=True,
        blank=True)
    Ultima_reuniao_de_alinhamento = models.DateField(
        null=True,
        blank=True)
    Usuario_representante_na_ultima_reuniao = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='presente',
        on_delete=models.CASCADE)
    Obs_do_fornecedor = models.TextField(
        null=True,
        blank=True)
    Data_de_cadastro_do_fornecedor = models.DateField(
        null=True,
        blank=True)