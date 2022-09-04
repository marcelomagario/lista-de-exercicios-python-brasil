"""
Exercício 12 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosListas

Foram anotados os nomes, as idades e alturas de de vários alunos.
Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses
alunos.

Mostre a média com uma casa decimal.

    >>> calcular_baixinhos_com_mais_de_13_anos(('Renzo', 39, 162))
    Média de altura: 162.0 centímetros.
    Não há nenhum aluno abaixo da média
    >>> calcular_baixinhos_com_mais_de_13_anos(('Renzo', 39, 162), ('Priscila', 33, 158))
    Média de altura: 160.0 centímetros.
    Existe(m) 1 aluno(s) com altura abaixo da média com mais de 13 anos:
    1. Priscila, com 158 centímetros e 33 ano(s) de idade
    >>> calcular_baixinhos_com_mais_de_13_anos(('Renzo', 39, 162), ('Priscila', 33, 158), ('Gigante', 20, 210))
    Média de altura: 176.7 centímetros.
    Existe(m) 2 aluno(s) com altura abaixo da média com mais de 13 anos:
    1. Renzo, com 162 centímetros e 39 ano(s) de idade
    2. Priscila, com 158 centímetros e 33 ano(s) de idade
    >>> calcular_baixinhos_com_mais_de_13_anos(
    ...     ('Renzo', 39, 162), ('Priscila', 33, 158), ('Gigante', 20, 210), ('Criança', 7, 100)
    ... )
    Média de altura: 157.5 centímetros.
    Não há nenhum aluno abaixo da média
    >>> calcular_baixinhos_com_mais_de_13_anos(
    ...     ('Renzo', 39, 162), ('Priscila', 33, 158), ('Gigante', 20, 210),
    ...     ('Criança', 7, 100), ("Shaquille O'Neal", 25, 216)
    ... )
    Média de altura: 169.2 centímetros.
    Existe(m) 2 aluno(s) com altura abaixo da média com mais de 13 anos:
    1. Renzo, com 162 centímetros e 39 ano(s) de idade
    2. Priscila, com 158 centímetros e 33 ano(s) de idade

"""

from statistics import mean
def calcular_baixinhos_com_mais_de_13_anos(*alunos):
    """Escreva aqui em baixo a sua solução"""
    alturas = []
    alunos_baixinhos = []

    for i in range(len(alunos)):
        alturas.append(alunos[i][2])
    media = mean(alturas)
    for i in range(len(alunos)):
        if alunos[i][1] >= 13 and alunos[i][2] < media:
            alunos_baixinhos.append(alunos[i]) # insere os alunos baixinhos na lista
    print(f'Média de altura: {media:.1f} centímetros.')
    if not alunos_baixinhos:
        print('Não há nenhum aluno abaixo da média')
    else:
        print(f'Existe(m) {len(alunos_baixinhos)} aluno(s) com altura abaixo da média com mais de 13 anos:')
    for i in range(len(alunos_baixinhos)):
        print(f'{i+1}. {alunos_baixinhos[i][0]}, com {alunos_baixinhos[i][2]} centímetros e {alunos_baixinhos[i][1]} ano(s) de idade')
