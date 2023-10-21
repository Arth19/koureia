from django.contrib import admin
from .models import (
    Funcionario, CategoriaServico, Servico, Cliente,
    Agendamento, Promocao, Produto, Venda,
    ItemVenda, Pagamento, Avaliacao
)

class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'telefone', 'email')
    search_fields = ('username', 'first_name', 'last_name', 'telefone')

class CategoriaServicoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'categoria')
    search_fields = ('nome',)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'data_nascimento')
    search_fields = ('nome', 'telefone')

class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'servico', 'funcionario', 'data_hora')
    search_fields = ('cliente__nome', 'servico__nome', 'funcionario__username')

class PromocaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'desconto_percentual', 'inicio_validade', 'fim_validade')
    search_fields = ('nome',)

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'quantidade_estoque')
    search_fields = ('nome',)

class VendaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'data_hora', 'total')
    search_fields = ('cliente__nome',)

class ItemVendaAdmin(admin.ModelAdmin):
    list_display = ('venda', 'produto', 'quantidade', 'preco_unitario')
    search_fields = ('produto__nome',)

class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('venda', 'data_hora', 'valor')
    search_fields = ('venda__cliente__nome',)

class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'servico', 'avaliacao')
    search_fields = ('cliente__nome', 'servico__nome')

# Registrar os modelos e as classes de administração personalizadas
admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(CategoriaServico, CategoriaServicoAdmin)
admin.site.register(Servico, ServicoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Agendamento, AgendamentoAdmin)
admin.site.register(Promocao, PromocaoAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Venda, VendaAdmin)
admin.site.register(ItemVenda, ItemVendaAdmin)
admin.site.register(Pagamento, PagamentoAdmin)
admin.site.register(Avaliacao, AvaliacaoAdmin)
