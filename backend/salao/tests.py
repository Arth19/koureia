import datetime
from django.utils import timezone  # Certifique-se de importar timezone assim
from django.forms import ValidationError
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
        self.funcionario = Funcionario.objects.create(username='func1', password='senha123', telefone='+5511912345678')
        self.cliente = Cliente.objects.create(nome='Cliente Teste', telefone='+5511987654321', data_nascimento='1990-01-01')
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

    def test_invalid_service_price(self):
        with self.assertRaises(ValidationError):
            servico_invalido = Servico.objects.create(nome='Serviço Inválido', preco='-50.00', categoria=self.categoria_servico)
            servico_invalido.full_clean()

    def test_invalid_agendamento_date(self):
        with self.assertRaises(ValidationError):
            agendamento_invalido = Agendamento.objects.create(
                cliente=self.cliente,
                servico=self.servico,
                funcionario=self.funcionario,
                data_hora=timezone.make_aware(datetime.datetime(2022, 10, 22, 10, 0))  # Agora usando datetime.datetime
            )
            agendamento_invalido.full_clean()

# Testes para a API
@override_settings(REST_FRAMEWORK={'DEFAULT_PERMISSION_CLASSES': []})
class APITestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.funcionario = Funcionario.objects.create_superuser(username='func1', password='senha123', telefone='+5511912345678')  # número de telefone atualizado
        self.client.force_authenticate(user=self.funcionario)

    def test_listagem_funcionarios(self):
        response = self.client.get(reverse('funcionario-list'))
        print(response.data)  # Adicionada linha para imprimir a resposta
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_criacao_funcionario(self):
        data = {
            'username': 'func2',
            'password': 'senha123',
            'telefone': '+5511987654321'  # número de telefone atualizado
        }
        response = self.client.post(reverse('funcionario-list'), data, format='json')
        print(response.data)  # Adicionada linha para imprimir a resposta
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
