"""
Exercício 45 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno
a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a
nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro
aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:

Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma com uma casa decimal.

Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A

    >>> corrigir(('Renzo','A','B','C','D','E','E','D','C','B','A' ))
    Aluno                 Nota
    Renzo                 10
    ---------------------------
    Média geral: 10.0
    Maior nota: 10
    Menor nota: 10
    Total de Alunos: 1
    >>> corrigir(
    ... ('Renzo','A','B','C','D','E','E','D','C','B','A' ),
    ... ('Fulano','A','B','C','D','E','E','D','C','B','B' ),
    ... )
    Aluno                 Nota
    Renzo                 10
    Fulano                 9
    ---------------------------
    Média geral: 9.5
    Maior nota: 10
    Menor nota: 9
    Total de Alunos: 2
"""


def corrigir(*provas):
    """Escreva aqui em baixo a sua solução"""
    gabarito = {
        1: 'A',
        2: 'B',
        3: 'C',
        4: 'D',
        5: 'E',
        6: 'E',
        7: 'D',
        8: 'C',
        9: 'B',
        10: 'A',
    }

    alunos_notas = {}
    maior_nota, menor_nota, total_alunos, media_nota = 0, 0, 0, 0
    for i in range(len(provas)):
        nota_contador = 0
        for n in range(1, len(provas[i])):
            # Verifica e contabiliza se a entrada é igual a resposta no gabarito.
            if provas[i][n] == gabarito.get(n):
                nota_contador += 1
        # Salva o nome e a nota do aluno no dicionário
        alunos_notas[provas[i][0]] = nota_contador
    maior_nota = max(alunos_notas.values())
    menor_nota = min(alunos_notas.values())
    total_alunos = len(alunos_notas)
    media_nota = (maior_nota + menor_nota) / 2
    print('Aluno                 Nota')
    for k, v in alunos_notas.items():
        print(f'{k:21s} {v:2d}')

    print('---------------------------')
    print(f'Média geral: {media_nota}')
    print(f'Maior nota: {maior_nota}')
    print(f'Menor nota: {menor_nota}')
    print(f'Total de Alunos: {total_alunos}')
