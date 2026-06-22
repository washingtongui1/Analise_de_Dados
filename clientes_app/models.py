from django.db import models


class Cliente(models.Model):
    id_cliente = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    cpf = models.CharField(max_length=14, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Cliente'

    def __str__(self):
        return self.nome or f'Cliente {self.id_cliente}'


class Fornecedor(models.Model):
    id_fornecedor = models.IntegerField(primary_key=True)
    nome_fornecedor = models.CharField(max_length=100, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Fornecedor'


class Funcionario(models.Model):
    id_funcionario = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    cargo = models.CharField(max_length=50, blank=True, null=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    data_admissao = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Funcionario'


class Produto(models.Model):
    id_produto = models.IntegerField(primary_key=True)
    nome_produto = models.CharField(max_length=100, blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    quantidade_estoque = models.IntegerField(blank=True, null=True)
    id_fornecedor = models.ForeignKey(
        Fornecedor,
        models.DO_NOTHING,
        db_column='id_fornecedor',
        blank=True,
        null=True,
    )

    class Meta:
        managed = False
        db_table = 'Produto'

    def __str__(self):
        return self.nome_produto or f'Produto {self.id_produto}'


class Venda(models.Model):
    id_venda = models.IntegerField(primary_key=True)
    data_venda = models.DateTimeField(blank=True, null=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    id_cliente = models.ForeignKey(
        Cliente,
        models.DO_NOTHING,
        db_column='id_cliente',
        blank=True,
        null=True,
    )
    id_funcionario = models.ForeignKey(
        Funcionario,
        models.DO_NOTHING,
        db_column='id_funcionario',
        blank=True,
        null=True,
    )

    class Meta:
        managed = False
        db_table = 'Venda'

    def __str__(self):
        return f'Venda {self.id_venda}'


class RelatorioVendas(models.Model):
    id_venda = models.IntegerField(primary_key=True)
    data_venda = models.DateTimeField(blank=True, null=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    nome_cliente = models.CharField(max_length=100, blank=True, null=True)
    nome_funcionario = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vw_relatorio_vendas'

    def __str__(self):
        return f'Venda {self.id_venda}'
