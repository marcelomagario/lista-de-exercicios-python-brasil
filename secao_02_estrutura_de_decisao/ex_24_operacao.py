"""
Exercício 24 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da
operação deve ser acompanhado de uma frase que diga se o número é:
  par ou ímpar;
  positivo ou negativo;
  inteiro ou decimal.

Mostre o restultado com duas casas decimais

    >>> fazer_operacao_e_classificar(2, 3, '+')
    Resultado: 5.00
    Número é impar, positivo e inteiro.
    >>> fazer_operacao_e_classificar(-4, 2, '/')
    Resultado: -2.00
    Número é par, negativo e inteiro.
    >>> fazer_operacao_e_classificar(0, 2, '*')
    Resultado: 0.00
    Número é par, neutro e inteiro.
    >>> fazer_operacao_e_classificar(-3.14, 2, '*')
    Resultado: -6.28
    Número é negativo e decimal.
    >>> fazer_operacao_e_classificar(3.14, 2, '-')
    Resultado: 1.14
    Número é positivo e decimal.

"""

def par_ou_impar(resultado):
    """" Função para checar se o número é par ou impar """
    if resultado % 2 == 0:
        return 'par'
    else:
        return 'impar'
def positivo_ou_negativo(resultado):
    """ Função para checar se o número é positivo ou negativo """
    if resultado > 0:
        return 'positivo'
    elif resultado < 0:
        return 'negativo'
    else:
        return 'neutro'

def decimal_ou_inteiro(resultado):
    """ Função para checar se o resultado é decimal ou inteiro """
    arredondamento = round(resultado)
    if arredondamento == resultado:
        return 'inteiro'
    else:
        return 'decimal'

def fazer_operacao_e_classificar(n_1: float, n_2: float, operacao: str):
    """Escreva aqui em baixo a sua solução"""
    if operacao == '+':
        resultado = n_1 + n_2
    elif operacao == '-':
        resultado = n_1 - n_2
    elif operacao == '/':
        resultado = n_1 / n_2
    elif operacao == '*':
        resultado = n_1 * n_2
    else:
        print ('Operador inválido')

    print(f'Resultado: {resultado:.2f}')
    tipo_par_impar = par_ou_impar(resultado)
    tipo_positivo_negativo = positivo_ou_negativo(resultado)
    tipo_decimal_inteiro = decimal_ou_inteiro(resultado)
    if tipo_decimal_inteiro == 'decimal':
        print(f'Número é {tipo_positivo_negativo} e {tipo_decimal_inteiro}.')
    else:
        print(f'Número é {tipo_par_impar}, {tipo_positivo_negativo} e {tipo_decimal_inteiro}.')
