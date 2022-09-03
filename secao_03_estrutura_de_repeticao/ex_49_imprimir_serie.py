"""
Exercício 49 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que mostre os n termos da Série a seguir:
    
    S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
    
    Imprima no final a soma da série.
    
    ----------------------------------
    | EXEMPLO                         |
    ----------------------------------
    | ENTRADA:                        |
    | n = 5                           |
    | SAIDA:                          |
    | S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 |
    | soma = 3.393650793650793        |
    ----------------------------------
    

    >>> imprimir_serie(5)
    S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9
    soma = 3.393650793650793
    >>> imprimir_serie(7)
    S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + 6/11 + 7/13
    soma = 4.477566877566877
    >>> imprimir_serie(3)
    S = 1/1 + 2/3 + 3/5
    soma = 2.2666666666666666
    >>> imprimir_serie(9)
    S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + 6/11 + 7/13 + 8/15 + 9/17
    soma = 5.540311975606093

"""
def imprimir_serie(n):
    """Escreva aqui em baixo a sua solução"""
    dividendo, divisor = [1], [1]
    novo_dividendo, novo_divisor, soma = 0, 0, 0
    serie_str = ''
    for i in range(0, n):
        novo_dividendo = dividendo[-1] + 1 # adiciona 1 ao ultimo elemento da lista
        dividendo.append(novo_dividendo)
        novo_divisor = divisor[-1] + 2 # adiciona 2 ao ultimo elemento da lista
        divisor.append(novo_divisor)
        serie_str += f'{dividendo[i]}/{divisor[i]} + '
        soma += dividendo[i]/divisor[i]
    print(f'S = {serie_str[:-3]}') # -3 é para tirar o último sinal de +
    print(f'soma = {soma}')

