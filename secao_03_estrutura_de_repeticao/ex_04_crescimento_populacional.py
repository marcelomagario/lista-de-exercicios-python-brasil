"""
Exercício 04 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a
população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o
número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas
de crescimento.

    >>> calcular_ano_ultrapassagem_populacional()
    'População de A, depois de 63 ano(s) será de 515033 pessoas, superando a de B, que será de 510964 pessoas'


"""


def calcular_ano_ultrapassagem_populacional() -> str:
    """Escreva aqui em baixo a sua solução"""
    populacao_a = 80_000
    taxa_a = 0.03
    populacao_b = 200_000
    taxa_b = 0.015
    qtde_de_anos = 0
    while populacao_b > populacao_a:
        aumento_anual_a = populacao_a * taxa_a
        populacao_a = populacao_a + aumento_anual_a
        aumento_anual_b = populacao_b * taxa_b
        populacao_b = populacao_b + aumento_anual_b
        qtde_de_anos = qtde_de_anos + 1
    else:
        return (
                f'População de A, depois de {qtde_de_anos} ano(s) será de {round(populacao_a)} pessoas,'
                f' superando a de B, que será de {round(populacao_b)} pessoas'
        )

