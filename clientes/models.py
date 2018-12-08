from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Categoria(models.Model):
    Nome_da_categoria = models.CharField(max_length=100)
    def __str__(self):
        return self.Nome_da_categoria
    Ativada = models.BooleanField()
    Obs_da_categoria = models.TextField()
    Data_de_cadastro_da_categoria = models.DateField()

class Clientes(models.Model):
    Categoria_do_cliente = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    Cliente_ativo = models.BooleanField()
    Nome_fantasia = models.CharField(max_length=100)
    def __str__(self):
        return self.Nome_fantasia
    Nome_do_cliente = models.CharField(max_length=100)
    Razao_social = models.CharField(max_length=100)
    Logo_do_cliente = models.ImageField(upload_to='upload/')
    Telefone_1 = PhoneNumberField()
    Telefone_2 = PhoneNumberField()
    Celular_1 = PhoneNumberField()
    Site_do_cliente = models.URLField()
    TIPOJURIDICODOCLIENTE = (
        ("MEI", "Micro Empreendedor Individual"),
        ("PF", "Pessoa Física"),
        ("SN", "Simples Nacional"),
    )
    Tipo_juridico_do_cliente = models.CharField(max_length=50, choices=TIPOJURIDICODOCLIENTE)
    Cnpj = models.CharField(max_length=100)
    Inscricao_estadual = models.CharField(max_length=50)
    RESPOSTACONTRATO = (
        ("SC", "Sem contrato"),
        ("EN", "Contrato em negociação"),
        ("PC", "Possui contrato"),
    )
    Possui_contrato = models.CharField(max_length=30, choices=RESPOSTACONTRATO)
    Contrato_ou_proposta_anexado = models.FileField(upload_to='upload/')
    Valor_total_do_contrato = models.FloatField()
    Endereco = models.CharField(max_length=300)
    CEP = models.CharField(max_length=100)
    Cidade = models.CharField(max_length=60)
    ESTADO = (
        ("AC", "Acre"),
        ("AL", "Alagoas"),
        ("AP", "Amapá"),
        ("AM", "Amazonas"),
        ("BA", "Bahia"),
        ("CE", "Ceará"),
        ("DF", "Distrito Federal"),
        ("ES", "Espírito Santo"),
        ("GO", "Goiás"),
        ("MA", "Maranhão"),
        ("MT", "Mato Grosso"),
        ("MS", "Mato Grosso do Sul"),
        ("MG", "Minas Gerais"),
        ("PA", "Pará"),
        ("PB", "Paraíba"),
        ("PR", "Paraná"),
        ("PE", "Pernambuco"),
        ("PI", "Piauí"),
        ("RJ", "Rio de Janeiro"),
        ("RS", "Rio Grande do Sul"),
        ("RN", "Rio Grande do Norte"),
        ("RO", "Rondônia"),
        ("SC", "Santa Catarina"),
        ("SP", "São Paulo"),
        ("SE", "fornecedorSergipe"),
        ("TO", "Tocantins"),
    )
    Estado = models.CharField(max_length=60, choices=ESTADO)
    Email_do_cliente = models.EmailField()
    Obs_do_cliente = models.TextField()
    Data_de_cadastro_do_cliente = models.DateField()