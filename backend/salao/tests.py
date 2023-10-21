# salao/tests.py

from django.test import TestCase, override_settings
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import (
    Funcionario,
    CategoriaServico,
    Servico,
    Cliente,
    Agendamento,
    Promocao,
    Produto,
    Venda,
    ItemVenda,
    Pagamento,
    Avaliacao,
)
from .serializers import (
    FuncionarioSerializer,
    CategoriaServicoSerializer,
    ServicoSerializer,
    ClienteSerializer,
    AgendamentoSerializer,
    PromocaoSerializer,
    ProdutoSerializer,
    VendaSerializer,
    ItemVendaSerializer,
    PagamentoSerializer,
    AvaliacaoSerializer,
)

# Testes para os modelos
class ModelTestCase(TestCase):

    def setUp(self):
        self.funcionario = Funcionario.objects.create(username='func1', password='senha123')
        self.cliente = Cliente.objects.create(nome='Cliente Teste', telefone='123456789', data_nascimento='1990-01-01')
        self.categoria_servico = CategoriaServico.objects.create(nome='Corte')
        self.servico = Servico.objects.create(nome='Corte de Cabelo', preco='50.00', categoria=self.categoria_servico)

    def test_criacao_funcionario(self):
        self.assertEqual(self.funcionario.username, 'func1')

    def test_criacao_cliente(self):
        self.assertEqual(self.cliente.nome, 'Cliente Teste')

    def test_criacao_servico(self):
        self.assertEqual(self.servico.nome, 'Corte de Cabelo')

    def test_agendamento(self):
        agendamento = Agendamento.objects.create(cliente=self.cliente, servico=self.servico, funcionario=self.funcionario, data_hora='2023-10-22T10:00')
        self.assertEqual(agendamento.cliente.nome, 'Cliente Teste')

# Testes para a API
@override_settings(REST_FRAMEWORK={'DEFAULT_PERMISSION_CLASSES': []})
class APITestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.funcionario = Funcionario.objects.create_superuser(username='func1', password='senha123')  # alterado para create_superuser
        self.client.force_authenticate(user=self.funcionario)

    def test_listagem_funcionarios(self):
        response = self.client.get(reverse('funcionario-list'))
        print(response.data)  # Adicionada linha para imprimir a resposta
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_criacao_funcionario(self):
        data = {
            'username': 'func2',
            'password': 'senha123',
            'telefone': '123456789'  # Adicionado campo telefone
        }
        response = self.client.post(reverse('funcionario-list'), data, format='json')
        print(response.data)  # Adicionada linha para imprimir a resposta
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

