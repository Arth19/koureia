from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from phonenumber_field.modelfields import PhoneNumberField

class Funcionario(AbstractUser):
    telefone = PhoneNumberField(blank=False, unique=True)

    def __str__(self):
        return self.username

class CategoriaServico(models.Model):
    nome = models.CharField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.nome

class Servico(models.Model):
    nome = models.CharField(max_length=255, db_index=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(CategoriaServico, on_delete=models.SET_NULL, null=True)

    def clean(self):
        if self.preco < 0:
            raise ValidationError({"preco": "O preço não pode ser negativo."})

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=255, db_index=True)
    telefone = PhoneNumberField(blank=False, unique=True)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome

class Agendamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_index=True)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, db_index=True)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True, db_index=True)
    data_hora = models.DateTimeField()

    def clean(self):
        if self.data_hora < timezone.now():
            raise ValidationError({"data_hora": "A data e hora do agendamento não podem estar no passado."})

    def __str__(self):
        return f"Agendamento de {self.cliente} para {self.servico} com {self.funcionario} em {self.data_hora}"

class Promocao(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    desconto_percentual = models.DecimalField(max_digits=5, decimal_places=2)
    inicio_validade = models.DateTimeField()
    fim_validade = models.DateTimeField()

    def clean(self):
        if self.inicio_validade >= self.fim_validade:
            raise ValidationError({"fim_validade": "A data de fim deve ser posterior à data de início."})

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_estoque = models.PositiveIntegerField(default=0)

    def clean(self):
        if self.preco < 0:
            raise ValidationError({"preco": "O preço não pode ser negativo."})

    def __str__(self):
        return self.nome

class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    data_hora = models.DateTimeField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Venda para {self.cliente} em {self.data_hora}"

class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, related_name='itens', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    
    def clean(self):
        if self.quantidade <= 0:
            raise ValidationError({"quantidade": "A quantidade deve ser um valor positivo."})

    def __str__(self):
        return f"Item de {self.produto} na venda {self.venda.id}"

class Pagamento(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pagamento de {self.valor} para a venda {self.venda.id}"

class Avaliacao(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, db_index=True)
    servico = models.ForeignKey(Servico, on_delete=models.SET_NULL, null=True, db_index=True)
    avaliacao = models.PositiveIntegerField()
    comentario = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = (('cliente', 'servico'),)
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'

    def clean(self):
        if not 1 <= self.avaliacao <= 5:
            raise ValidationError({"avaliacao": "A avaliação deve estar entre 1 e 5."})

    def __str__(self):
        return f"Avaliação de {self.cliente} para {self.servico}"
