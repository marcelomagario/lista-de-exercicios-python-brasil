"""
Exercício 21 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo
é de 1 real e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma
nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10,
uma nota de 5 e quatro notas de 1.

    >>> calcular_troco(256)
    '2 notas de R$ 100, 1 nota de R$ 50, 1 nota de R$ 5 e 1 nota de R$ 1'
    >>> calcular_troco(1)
    '1 nota de R$ 1'
    >>> calcular_troco(5)
    '1 nota de R$ 5'
    >>> calcular_troco(10)
    '1 nota de R$ 10'
    >>> calcular_troco(11)
    '1 nota de R$ 10 e 1 nota de R$ 1'
    >>> calcular_troco(399)
    '3 notas de R$ 100, 1 nota de R$ 50, 4 notas de R$ 10, 1 nota de R$ 5 e 4 notas de R$ 1'
"""

def rreplace(s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return new.join(li)

def calcular_troco(valor: int) -> str:
    """Escreva aqui em baixo a sua solução"""
   # import math
    lista_de_valores = [100, 50, 10, 5, 1]
    lista_contador = [0, 0, 0, 0, 0]
    mensagem = ''

    for i in range(len(lista_de_valores)):
        if valor >= lista_de_valores[i]:
            lista_contador[i] = valor // lista_de_valores[i]  # 256//100 = 2 -> lista_contador[0] = 2
            valor = valor % lista_de_valores[i]
        else:
            lista_contador[i] = 0
    lista_str = ['notas' if nota > 1 else 'nota' for nota in lista_contador]
    mensagem = ''
    for n in range(len(lista_contador)):
        if lista_contador[n] > 0:
            mensagem += f'{lista_contador[n]} {lista_str[n]} de R$ {lista_de_valores[n]}, '


    mensagem = rreplace(mensagem, ', ', '', 1)

    return f"{rreplace(mensagem, ', ', ' e ', 1)}"


