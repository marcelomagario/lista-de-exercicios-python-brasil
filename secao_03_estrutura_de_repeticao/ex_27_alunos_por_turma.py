"""
Exercício 27 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao
Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade
de alunos para cada turma. As turmas não podem ter mais de 40 alunos e devem ter ao menos um aluno.
Arredonde o valor da média para baixo.
    >>> from secao_03_estrutura_de_repeticao import ex_27_alunos_por_turma
    >>> entradas = ['1', '1']
    >>> ex_27_alunos_por_turma.input = lambda k: entradas.pop()
    >>> ex_27_alunos_por_turma.calcular_media_de_alunos_por_turma()
    Número de turmas: 1
    Média de alunos por turma: 1
    >>> entradas = ['40', '40', '2']
    >>> ex_27_alunos_por_turma.input = lambda k: entradas.pop()
    >>> ex_27_alunos_por_turma.calcular_media_de_alunos_por_turma()
    Número de turmas: 2
    Média de alunos por turma: 40
    >>> entradas = ['10', '20', '30', '40', '-1', '4']
    >>> ex_27_alunos_por_turma.input = lambda k: entradas.pop()
    >>> ex_27_alunos_por_turma.calcular_media_de_alunos_por_turma()
    Número de turmas: 4
    Uma turma deve ter de 1 a 40 alunos, não é possível ter -1 alunos
    Média de alunos por turma: 25
    >>> entradas = ['10', '20', '30', '0', '41', '3']
    >>> ex_27_alunos_por_turma.input = lambda k: entradas.pop()
    >>> ex_27_alunos_por_turma.calcular_media_de_alunos_por_turma()
    Número de turmas: 3
    Uma turma deve ter de 1 a 40 alunos, não é possível ter 41 alunos
    Uma turma deve ter de 1 a 40 alunos, não é possível ter 0 alunos
    Média de alunos por turma: 20
"""
from statistics import mean
def calcular_media_de_alunos_por_turma():
    # solução do Renzo. A minha está comentada lá embaixo. A minha soluçao foi de acordo com o doctest.
    # O usuário entra com uma lista e o último elemento da lista é o número de turmas.
    """Escreva aqui em baixo a sua solução"""
    numero_de_turmas = int(input('Digite o número de turmas: '))
    turmas = []
    print(f'Número de turmas: {numero_de_turmas}')
    while len(turmas) < numero_de_turmas:
        turma_atual = len(turmas) + 1
        numero_de_alunos_turma_atual = int(input(f'Digite quantos alunos estão na turma {turma_atual}: '))
        if not (1 <= numero_de_alunos_turma_atual <= 40):
            print(f'Uma turma deve ter de 1 a 40 alunos, não é possível ter {numero_de_alunos_turma_atual} alunos')
        else:
            turmas.append(numero_de_alunos_turma_atual)

    media_alunos_por_turma = int(mean(turmas))

    print(f'Média de alunos por turma: {media_alunos_por_turma}')

    # entradas = [10, 20, 30, 0, 41, 3]
    # qtde_turmas = entradas.pop(-1)
    # entradas.reverse()
    # total_de_alunos = 0
    # media_de_alunos = 0
    # for i in range(len(entradas)):
    #     if (entradas[i] > 0) and (entradas[i] <= 40):
    #         total_de_alunos += entradas[i]
    #     else:
    #         print(f'Número inválido {entradas[i]}')
    # media_de_alunos = int((total_de_alunos / qtde_turmas))
    # print(qtde_turmas)
    # print(media_de_alunos)