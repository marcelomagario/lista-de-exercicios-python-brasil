"""
Exercício 07 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia três números e mostre o maior e o menor deles.

    >>> calcular_maior_de_3_numeros(2,3, 5)
    Maior: 5
    Menor: 2
    >>> calcular_maior_de_3_numeros(-1, -10, -2)
    Maior: -1
    Menor: -10
    >>> calcular_maior_de_3_numeros(-5, 3, 0)
    Maior: 3
    Menor: -5
    >>> calcular_maior_de_3_numeros(7, -14, 15)
    Maior: 15
    Menor: -14
"""


def calcular_maior_de_3_numeros(numero1, numero2, numero3):
    """Escreva aqui em baixo a sua solução"""
    if (numero1 > numero2 and numero1 > numero3):
        maior = numero1
    elif  (numero2 > numero1 and numero2 > numero3):
        maior = numero2
    elif  (numero3 > numero1 and numero3 > numero2):
        maior = numero3

    if (numero1 < numero2 and numero1 < numero3):
        menor = numero1
    elif  (numero2 < numero1 and numero2 < numero3):
        menor = numero2
    elif  (numero3 < numero1 and numero3 < numero2):
        menor = numero3

    print(f'Maior: {maior}')
    print(f'Menor: {menor}')
