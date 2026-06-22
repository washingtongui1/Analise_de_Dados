from django.urls import path

from .views import analise_vendas, clientes_view, lista_dados, produtos_view, vendas_view

urlpatterns = [
    path('', lista_dados, name='lista_dados'),
    path('clientes/', clientes_view, name='clientes'),
    path('produtos/', produtos_view, name='produtos'),
    path('vendas/', vendas_view, name='vendas'),
    path('analise-vendas/', analise_vendas, name='analise_vendas'),
]