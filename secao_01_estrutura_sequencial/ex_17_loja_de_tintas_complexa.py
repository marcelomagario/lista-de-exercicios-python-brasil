"""
Exercício 17 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o custo seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

    >>> from secao_01_estrutura_sequencial import ex_17_loja_de_tintas_complexa
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '100'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 19 litros de tinta.
    Você pode comprar 2 lata(s) de 18 litros a um custo de R$ 160. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 6 lata(s) de 3.6 litros a um custo de R$ 150. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 1 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 105. Vão sobrar 2.6 litro(s) de tinta.
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '200'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 37 litros de tinta.
    Você pode comprar 3 lata(s) de 18 litros a um custo de R$ 240. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 11 lata(s) de 3.6 litros a um custo de R$ 275. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 2 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 185. Vão sobrar 2.6 litro(s) de tinta.

"""


def calcular_latas_e_preco_de_tinta():
    """Escreva aqui em baixo a sua solução"""
    import math
    area = float(input('Informe a area (m2) a ser pintada: '))
    area_com_folga = area * 1.1

    litros_por_metro = 6
    litros_necessarios = math.ceil(area_com_folga / litros_por_metro)
    litros_por_lata = 18
    qtde_latas = math.ceil(litros_necessarios / litros_por_lata) # Arredondar para cima usando math.ceil
    litros_por_galao = 3.6
    qtde_galoes = math.ceil(litros_necessarios / litros_por_galao) # Arredondar para cima usando math.ceil
    preco_total_com_latas = qtde_latas * 80
    preco_total_com_galoes = qtde_galoes * 25
    sobra_das_latas = (qtde_latas * litros_por_lata) - litros_necessarios
    sobra_dos_galoes = (qtde_galoes * litros_por_galao) - litros_necessarios
    print(f'Você deve comprar {litros_necessarios} litros de tinta.')
    print(f'Você pode comprar {qtde_latas} lata(s) de 18 litros a um custo de R$ {preco_total_com_latas}. Vão sobrar {sobra_das_latas:.1f} litro(s) de tinta.')
    print(f'Você pode comprar {qtde_galoes} lata(s) de 3.6 litros a um custo de R$ {preco_total_com_galoes}. Vão sobrar {sobra_dos_galoes:.1f} litro(s) de tinta.')

  
    # Comprando pensando em economizar tinta
    qtde_latas = math.floor (litros_necessarios / litros_por_lata)
    valor_de_latas = qtde_latas * 80
    litros_faltantes = litros_necessarios % litros_por_lata
    qtde_galoes = math.ceil (litros_faltantes / litros_por_galao)
    valor_de_galoes = qtde_galoes * 25
    valor_total = valor_de_latas + valor_de_galoes
    sobra_de_tinta = (qtde_latas * litros_por_lata) + (qtde_galoes * litros_por_galao) - litros_necessarios
    print (f'Para menor custo, você pode comprar {qtde_latas} lata(s) de 18 litros e {qtde_galoes} galão(ões) de 3.6 litros a um custo de R$ {valor_total:.0f}. Vão sobrar {sobra_de_tinta:.1f} litro(s) de tinta.')
