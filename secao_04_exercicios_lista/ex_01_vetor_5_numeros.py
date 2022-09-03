"""
Exercício 01 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosListas

Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

    >>> ler_5_valores()

"""
def ler_5_valores():
    """Escreva aqui em baixo a sua solução"""
    vetor = []
    for i in range(0, 5):
        vetor += [int(input('Digite 1 número inteiro: '))]
    print(vetor)

