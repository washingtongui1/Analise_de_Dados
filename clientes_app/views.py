import json

from django.db.models import Count, Sum
from django.shortcuts import render

from .models import Cliente, Produto, RelatorioVendas, Venda


def _render_with_partial(request, full_template, partial_template, context):
    if request.headers.get('HX-Request') == 'true':
        return render(request, partial_template, context)
    return render(request, full_template, context)


def lista_dados(request):
    return clientes_view(request)


def clientes_view(request):
    clientes = Cliente.objects.all().order_by('id_cliente')
    context = {
        'clientes': clientes,
        'active_tab': 'clientes',
    }
    return _render_with_partial(
        request,
        'clientes.html',
        'partials/clientes_partial.html',
        context,
    )


def produtos_view(request):
    produtos = Produto.objects.all().order_by('id_produto')
    context = {
        'produtos': produtos,
        'active_tab': 'produtos',
    }
    return _render_with_partial(
        request,
        'produtos.html',
        'partials/produtos_partial.html',
        context,
    )


def vendas_view(request):
    vendas = Venda.objects.all().order_by('id_venda')
    context = {
        'vendas': vendas,
        'active_tab': 'vendas',
    }
    return _render_with_partial(
        request,
        'vendas.html',
        'partials/vendas_partial.html',
        context,
    )


def analise_vendas(request):
    relatorio = RelatorioVendas.objects.all().order_by('id_venda')

    dados_por_funcionario = (
        relatorio.values('nome_funcionario')
        .annotate(
            total_vendas=Count('id_venda', distinct=True),
            faturamento=Sum('valor_total'),
        )
        .order_by('nome_funcionario')
    )

    labels = [item['nome_funcionario'] for item in dados_por_funcionario]
    qtd = [item['total_vendas'] for item in dados_por_funcionario]
    faturamento = [float(item['faturamento'] or 0) for item in dados_por_funcionario]

    context = {
        'relatorio': relatorio,
        'labels': json.dumps(labels),
        'qtd': json.dumps(qtd),
        'faturamento': json.dumps(faturamento),
        'active_tab': 'analise_vendas',
    }
    return render(request, 'analise_vendas.html', context)
