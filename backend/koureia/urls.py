from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

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

schema_view = get_schema_view(
   openapi.Info(
      title="API Koureia",
      default_version='v1',
      description="API para gerenciamento de um salão de beleza",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contato@seusalao.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),  # incluindo o path para o admin
    path('', include(router.urls)),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
