"""
Exercício 09 da seção de strings da Python Brasil:
https://wiki.python.org.br/ExerciciosComStrings

Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx
e indique se é um número válido ou inválido através da validação dos dígitos verificadores
e dos caracteres de formatação.

    >>> validar_cpf('734.289.251-30')
    True


    >>> validar_cpf('732.289.294-10')
    False


    >>> validar_cpf('44986045040')
    True


    >>> validar_cpf('6693171008')
    False


"""
import string


def validar_cpf(cpf):
    """Escreva aqui em baixo a sua solução"""
    verificador_1, verificador_2 = 0, 0
    cpf_str = ''.join([i for i in cpf if i not in string.punctuation])  # retirar pontuação
    # cpf_int = int(cpf_str)
    lista_numeros = [int(i) for i in str(cpf_str)]
    primeiro_verificador = list(range(1, 10))
    segundo_verificador = list(range(10))
    # Identificar o valor do 1 digito
    for i in range(0, 9):
        verificador_1 += (lista_numeros[i] * primeiro_verificador[i])
    verificador_1 = verificador_1 % 11
    # Identificar o valor do 2 digito
    for i in range(0, 10):
        verificador_2 += (lista_numeros[i] * segundo_verificador[i])
    verificador_2 = verificador_2 % 11
    # comparar o verificador com os digitos do CPF
    if verificador_1 == lista_numeros[-2] and verificador_2 == lista_numeros[-1]:
        return True
    else:
        return False
    # print(verificador_1)
    # print(verificador_2)
