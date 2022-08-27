"""
Exercício 28 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao
Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em
cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.
Mostre os valores monetórios com duas casas decimais..
    >>> from secao_03_estrutura_de_repeticao import ex_28_colecao_de_cds
    >>> lista_entradas = ['1', '1']
    >>> ex_28_colecao_de_cds.input = lambda k: lista_entradas.pop()
    >>> ex_28_colecao_de_cds.calcular_estatisticas_colecao_de_cd()
    Número de cds: 1
    Valor total da coleção: R$ 1.00
    Custo médio dos cds: R$ 1.00
    >>> lista_entradas = ['40', '40', '2']
    >>> ex_28_colecao_de_cds.input = lambda k: lista_entradas.pop()
    >>> ex_28_colecao_de_cds.calcular_estatisticas_colecao_de_cd()
    Número de cds: 2
    Valor total da coleção: R$ 80.00
    Custo médio dos cds: R$ 40.00
    >>> lista_entradas = ['10', '20', '30', '40', '4']
    >>> ex_28_colecao_de_cds.input = lambda k: lista_entradas.pop()
    >>> ex_28_colecao_de_cds.calcular_estatisticas_colecao_de_cd()
    Número de cds: 4
    Valor total da coleção: R$ 100.00
    Custo médio dos cds: R$ 25.00
    >>> lista_entradas = ['10', '20', '30', '3']
    >>> ex_28_colecao_de_cds.input = lambda k: lista_entradas.pop()
    >>> ex_28_colecao_de_cds.calcular_estatisticas_colecao_de_cd()
    Número de cds: 3
    Valor total da coleção: R$ 60.00
    Custo médio dos cds: R$ 20.00
"""
from statistics import mean


def calcular_estatisticas_colecao_de_cd():
    """Escreva aqui em baixo a sua solução"""
    qtde_cds = int(input('Número de cds: '))
    cds = []
    print(f'Número de cds: {qtde_cds}')
    while len(cds) < qtde_cds:
        cd_atual = len(cds) + 1
        preco_do_cd = int(input(f'Digite o preco do CD {cd_atual}: '))
        cds.append(preco_do_cd)

    valor_total_cd = sum(cds)
    media_preco_cd = int(mean(cds))
    print(f'Valor total da coleção: R$ {valor_total_cd:.2f}')
    print(f'Custo médio dos cds: R$ {media_preco_cd:.2f}')
