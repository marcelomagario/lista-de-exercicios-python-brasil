"""
Exercício 13 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosListas

Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
Após isto, calcule e MOSTRE A MÉDIA ANUAL das temperaturas e MOSTRE TODAS AS TEMPERATURAS ACIMA DA MÉDIA ANUAL,
e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

-as temperaturas só serão dadas em inteiro
-todos os meses do ano serão passados à funçao, começando de janeiro e terminando em dezembro.
 Todos seguidos de sua temperatura mensal

(Funçoês recomendadas para estudo:
    - .ljust()
    - enumerate()
    - sum()
    - len()


    >>> from secao_04_exercicios_lista import ex_13_media_de_temperaturas_anual

    >>> meses_vs_temperaturas = ['25', '33', '19', '16', '15', '20', '25', '29', '25', '27', '33', '30']
    >>> ex_13_media_de_temperaturas_anual.input = lambda k: meses_vs_temperaturas.pop()
    >>> ex_13_media_de_temperaturas_anual.temperaturas_acima_da_media()
    Média anual: 24.75 Graus
     1 - Janeiro:       30°
     2 - Fevereiro:     33°
     3 - Março:         27°
     4 - Abril:         25°
     5 - Maio:          29°
     6 - Junho:         25°
    11 - Novembro:      33°
    12 - Dezembro:      25°
    >>> meses_vs_temperaturas = ['25', '33', '19', '16', '15', '20', '25', '29', '25', '27', '33', '35']
    >>> ex_13_media_de_temperaturas_anual.input = lambda k: meses_vs_temperaturas.pop()
    >>> ex_13_media_de_temperaturas_anual.temperaturas_acima_da_media()
    Média anual: 25.17 Graus
     1 - Janeiro:       35°
     2 - Fevereiro:     33°
     3 - Março:         27°
     5 - Maio:          29°
    11 - Novembro:      33°

"""

from statistics import mean
def temperaturas_acima_da_media():
    """Escreva aqui sua solução: """
    meses = [' 1 - Janeiro: ', ' 2 - Fevereiro: ', ' 3 - Março: ', ' 4 - Abril: ', ' 5 - Maio: ', ' 6 - Junho: ', ' 7 - Julho: ', ' 8 - Agosto: ', ' 9 - Setembro: ', '10 - Outubro: ',  '11 - Novembro: ', '12 - Dezembro: ']
    todas_temp = []
    temp_acima_da_media = []
    media = 0.
    for i in range(12):
        temp = int(input('Entre com as temperaturas: '))
        todas_temp.append(temp)

    media = mean(todas_temp)
    print(f'Média anual: {media:.2f} Graus')
    for i in range(len(todas_temp)):
        if todas_temp[i] > media:
            print(f'{meses[i]:<14s} {todas_temp[i]:>50}°')



# languages = ['Python', 'Java', 'JavaScript']
#
# enumerate_prime = enumerate(languages, start=1)
#
# # convert enumerate object to list
# print(list(enumerate_prime))
#
# # Output: [(0, 'Python'), (1, 'Java'), (2, 'JavaScript')]