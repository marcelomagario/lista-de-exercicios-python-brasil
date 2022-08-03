"""
Exercício 11 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
 1) o produto do dobro do primeiro com metade do segundo;
 2) a soma do triplo do primeiro com o terceiro;
 3) o terceiro elevado ao cubo.

 Apresente os resultados com duas casas decimais

    >>> from secao_01_estrutura_sequencial import ex_11_contas_matematicas
    >>> numeros = ['3.14', '43', '42']
    >>> ex_11_contas_matematicas.input = lambda k: numeros.pop()
    >>> ex_11_contas_matematicas.calcular_formulas()
    O produto do dobro do primeiro com metade do segundo é 1806.00
    A soma do triplo do primeiro com o terceiro é 129.14
    O terceiro elevado ao cubo é 30.96

"""


def calcular_formulas():
    """Escreva aqui em baixo a sua solução"""
    numero1_inteiro = int(input('Escolha um número inteiro: '))
    numero2_inteiro = int(input('Escolha um novamente um número inteiro: '))
    numero3_real = float(input('Agora escolha um número real: '))

    resultado_a = (numero1_inteiro * 2) * (numero2_inteiro / 2)
    resultado_b = (numero1_inteiro * 3) + numero3_real
    resultado_c = numero3_real ** 3

    print(f'O produto do dobro do primeiro com metade do segundo é {resultado_a:.2f}')
    print(f'A soma do triplo do primeiro com o terceiro é {resultado_b:.2f}')
    print(f'O terceiro elevado ao cubo é {resultado_c:.2f}')


