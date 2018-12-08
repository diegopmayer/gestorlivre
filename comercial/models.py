from django.db import models
from clientes.models import Clientes

class Produto(models.Model):
    Nome_do_produto = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.Nome_do_produto
    Produto_ativo = models.BooleanField()
    Valor_de_custo = models.FloatField(null=True, blank=True)
    Valor_de_venda = models.FloatField(null=True, blank=True)
    Manual_tecnico_do_produto = models.FileField(upload_to='upload/', null=True, blank=True)
    Imagem_do_produto = models.ImageField(upload_to='upload/', null=True, blank=True)
    Link_para_produto_no_site = models.URLField(null=True, blank=True)
    Obs_do_produto = models.TextField(null=True, blank=True)
    Data_de_cadastro_do_produto = models.DateField(null=True, blank=True)

class Pedido(models.Model):
    Descricao_do_pedido = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.Descricao_do_pedido
    Cliente_do_pedido = models.ForeignKey(Clientes, on_delete=models.CASCADE, null=True, blank=True)
    Produto_pedido = models.ForeignKey(Produto, on_delete=models.CASCADE, null=True, blank=True)
    METODODEENTREGA = (
        ("CT", "Correios"),
        ("SR", "Suporte remoto"),
        ("SF", "Licença de software"),
        ("PS", "Presencial"),
        ("PL", "Produto na loja")
    )
    Metodo_de_entrega = models.CharField(max_length=100, choices=METODODEENTREGA, null=True, blank=True)
    Data_prevista_para_entrega = models.DateField(null=True, blank=True)
    Data_de_cadastro_do_pedido = models.DateField(null=True, blank=True)
