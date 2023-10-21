from rest_framework import viewsets, permissions
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

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    permission_classes = [permissions.IsAdminUser]

class CategoriaServicoViewSet(viewsets.ModelViewSet):
    queryset = CategoriaServico.objects.all()
    serializer_class = CategoriaServicoSerializer
    permission_classes = [permissions.IsAuthenticated]

class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer

class PromocaoViewSet(viewsets.ModelViewSet):
    queryset = Promocao.objects.all()
    serializer_class = PromocaoSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer

class ItemVendaViewSet(viewsets.ModelViewSet):
    queryset = ItemVenda.objects.all()
    serializer_class = ItemVendaSerializer

class PagamentoViewSet(viewsets.ModelViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer

class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
