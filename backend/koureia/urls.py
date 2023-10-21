from django.contrib import admin
from django.urls import path, include

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from salao.views import (
    FuncionarioViewSet,
    CategoriaServicoViewSet,
    ServicoViewSet,
    ClienteViewSet,
    AgendamentoViewSet,
    PromocaoViewSet,
    ProdutoViewSet,
    VendaViewSet,
    ItemVendaViewSet,
    PagamentoViewSet,
    AvaliacaoViewSet,
)

router = DefaultRouter()
router.register(r'funcionarios', FuncionarioViewSet)
router.register(r'categorias-servico', CategoriaServicoViewSet)
router.register(r'servicos', ServicoViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'agendamentos', AgendamentoViewSet)
router.register(r'promocoes', PromocaoViewSet)
router.register(r'produtos', ProdutoViewSet)
router.register(r'vendas', VendaViewSet)
router.register(r'itens-venda', ItemVendaViewSet)
router.register(r'pagamentos', PagamentoViewSet)
router.register(r'avaliacoes', AvaliacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
