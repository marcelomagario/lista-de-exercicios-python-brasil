"""
Exercício 23 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

    >>> primos, divisoes = calcular_primos_e_divisoes(0)
    >>> primos
    ''
    >>> divisoes
    0
    >>> primos, divisoes = calcular_primos_e_divisoes(1)
    >>> primos
    ''
    >>> divisoes
    0
    >>> primos, divisoes = calcular_primos_e_divisoes(2)
    >>> primos
    '2'
    >>> divisoes
    0
    >>> primos, divisoes = calcular_primos_e_divisoes(3)
    >>> primos
    '2, 3'
    >>> divisoes <= 1
    True
    >>> primos, divisoes = calcular_primos_e_divisoes(4)
    >>> primos
    '2, 3'
    >>> divisoes <= 3
    True
    >>> primos, divisoes = calcular_primos_e_divisoes(5)
    >>> primos
    '2, 3, 5'
    >>> divisoes <= 6
    True

"""
from typing import Tuple


def calcular_primos_e_divisoes(n: int) -> Tuple[str, int]:
    """Escreva aqui em baixo a sua solução"""

    # Usada solução do Crivo de Erastótenes

    primos = []
    divisoes = 0
    if n > 1:
        candidatos_a_primos = list(range(3, n + 1, 2))
        candidatos_a_primos.reverse()
        candidatos_a_primos.append(2)
        while len(candidatos_a_primos) > 0:
            primo = candidatos_a_primos.pop()
            primos.append(primo)
            divisoes += len(candidatos_a_primos)
            candidatos_a_primos = [n for n in candidatos_a_primos if n % 2 != 0]

    return ', '.join(map(str, primos)), divisoes

#  Minha solução usando a reaproveitando a função do exercício anterior.
# intervalo = 100
# numeros_primos = []
# qtde_nao_primos = 0
#
# def eh_primo(n: int) -> bool:
#     """Escreva aqui em baixo a sua solução"""
#     if n < 2:
#         return False
#     elif n ==2:
#         return True
#     for i in range(2, n):
#         if (n % i) == 0:
#             return False
#     else:
#         return True
#
# for i in range(intervalo):
#     if eh_primo(i):
#         numeros_primos.append(i)
#     else:
#         qtde_nao_primos += 1
#
# print(intervalo)
# print(numeros_primos) # Imprimi todos os números primos do intervalo.
# print(qtde_nao_primos)

