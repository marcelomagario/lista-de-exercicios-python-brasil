"""
Exercício 09 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosListas

Faça um Programa que receba um vestor de números inteiros, calcule e mostre a soma dos quadrados dos elementos do
vetor.

    >>> calcular_soma_de_quadrados([])
    0
    >>> calcular_soma_de_quadrados([1])
    1
    >>> calcular_soma_de_quadrados([1, 2])
    5
    >>> calcular_soma_de_quadrados(list(range(10)))
    285

"""


def calcular_soma_de_quadrados(inteiros: list) -> int:
    """Escreva aqui em baixo a sua solução"""
    lista_quadrados = []
    for i in range(len(inteiros)):
        quadrado = inteiros[i] ** 2
        lista_quadrados.append(quadrado)
    soma = sum(lista_quadrados)
    print(soma)
