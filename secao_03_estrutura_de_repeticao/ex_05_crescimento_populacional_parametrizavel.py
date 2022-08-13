"""
Exercício 05 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Altere o programa anterior (ex_04_crescimento_populacional) permitindo ao usuário informar as populações e as taxas de
crescimento iniciais. Valide a entrada (crescimento do país A precisa ser maior que a do país B. Pense na razão dessa
restrição).

    >>> calcular_ano_ultrapassagem_populacional(80_000, 0.03, 200_000, 0.015)
    'População de A, depois de 63 ano(s) será de 515033 pessoas, superando a de B, que será de 510964 pessoas'
    >>> calcular_ano_ultrapassagem_populacional(80_000, 0.03, 200_000, 0.04)
    'A taxa de crescimento do país B (4.0%) deve ser menor do que a do país A (3.0%)'
    >>> calcular_ano_ultrapassagem_populacional(80_000, 0.05, 200_000, 0.015)
    'População de A, depois de 28 ano(s) será de 313610 pessoas, superando a de B, que será de 303444 pessoas'
    >>> calcular_ano_ultrapassagem_populacional(800_000, 0.05, 200_000, 0.015)
    'População de A, depois de 0 ano(s) será de 800000 pessoas, superando a de B, que será de 200000 pessoas'


"""

def calcular_ano_ultrapassagem_populacional(
        populacao_a: int, taxa_a: float, populacao_b,
        taxa_b: float) -> str:
    """Escreva aqui em baixo a sua solução"""
    if populacao_b > populacao_a and taxa_b > taxa_a:
        return f'A taxa de crescimento do país B ({taxa_b * 100}%) deve ser menor do que a do país A ({taxa_a * 100}%)'
    else:
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
