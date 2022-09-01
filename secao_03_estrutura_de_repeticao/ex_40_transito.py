"""
Exercício 40 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os
1) seguintes dados:
2) Código da cidade;
3) Número de veículos de passeio (em 1999);
4) Número de acidentes de trânsito com vítimas (em 1999).

Deseja-se saber:

1) Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
2) Qual a média de veículos nas cinco cidades juntas;
3) Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

Mostre os valores com uma casa decimail

    >>> calcular_estatisticas(('SJC', 190_000, 300), ('SP', 1_000_000, 2_000 ),
    ... ('BH', 800_000, 1000), ('FZ', 600_000, 700), ('FL', 150_000, 900)
    ... )
    O maior índice de acidentes é de FL, com 6.0 acidentes por mil carros.
    O menor índice de acidentes é de FZ, com 1.2 acidentes por mil carros.
    O média de veículos por cidade é de 548000.
    A média de acidentes total nas cidades com menos de 150 mil carros é de 900.0 acidentes.
"""
from operator import itemgetter
def calcular_estatisticas(*cidades):
    """Escreva aqui em baixo a sua solução"""
    total_de_veiculos, total_acidentes_cidade_pequena = 0, 0
    lista_indices, lista_total_acidentes = [], []
    limite_cidade_pequena = 150_000

    for n in range(len(cidades)):
        indice = cidades[n][2] / (cidades[n][1] / 1000)
        cidade_correspondente = cidades[n][0]
        novo_indice_cidade = (cidade_correspondente, indice)
        lista_indices.append(novo_indice_cidade)
        total_de_veiculos += cidades[n][1]
        if cidades[n][1] <= limite_cidade_pequena:
            lista_total_acidentes.append(cidades[n][2])

    maior_indice = max(lista_indices, key=itemgetter(1))
    menor_indice = min(lista_indices, key=itemgetter(1))
    media_de_veiculos = total_de_veiculos / len(cidades)
    total_acidentes_cidade_pequena = sum(lista_total_acidentes)
    media_acidentes_cidade_pequena = total_acidentes_cidade_pequena / len(lista_total_acidentes)

    print(f'O maior índice de acidentes é de {maior_indice[0]}, com {maior_indice[1]:.1f} acidentes por mil carros.')
    print(f'O menor índice de acidentes é de {menor_indice[0]}, com {menor_indice[1]:.1f} acidentes por mil carros.')
    print(f'O média de veículos por cidade é de {media_de_veiculos:.0f}.')
    print(f'A média de acidentes total nas cidades com menos de 150 mil carros é de {media_acidentes_cidade_pequena} acidentes.')
