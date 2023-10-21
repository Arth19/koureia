# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class Funcionario(AbstractUser):
    telefone = models.CharField(max_length=15)
    # Outros campos específicos dos funcionários

class CategoriaServico(models.Model):
    nome = models.CharField(max_length=255)

class Servico(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(CategoriaServico, on_delete=models.SET_NULL, null=True)

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField()

class Agendamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True)
    data_hora = models.DateTimeField()

class Promocao(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    desconto_percentual = models.DecimalField(max_digits=5, decimal_places=2)
    inicio_validade = models.DateTimeField()
    fim_validade = models.DateTimeField()

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_estoque = models.PositiveIntegerField()

class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    data_hora = models.DateTimeField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, related_name='itens', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

class Pagamento(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

class Avaliacao(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    servico = models.ForeignKey(Servico, on_delete=models.SET_NULL, null=True)
    avaliacao = models.PositiveIntegerField()
    comentario = models.TextField(null=True, blank=True)
