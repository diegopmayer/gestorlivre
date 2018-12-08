from django.db import models

class Item(models.Model):
    Nome_do_item = models.CharField(
        max_length=100,
        null=True,
        blank=True)
    def __str__(self):
        return self.Nome_do_item

    Valor_pago = models.FloatField(
        null=True,
        blank=True)
    Nota_fiscal_do_item = models.FileField(
        null=True,
        blank=True)
    Imagem_do_item = models.ImageField(
        upload_to='upload/',
        null=True,
        blank=True)
    Obs_do_item = models.TextField(
        null=True,
        blank=True)
    Data_de_cadastro_do_item = models.DateField(
        null=True,
        blank=True)