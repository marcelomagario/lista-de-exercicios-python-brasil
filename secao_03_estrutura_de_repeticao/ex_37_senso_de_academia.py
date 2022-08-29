"""
Exercício 37 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais 
magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu nome, sua altura e 
seu peso. 
O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo nome. Ao encerrar o programa 
também deve ser informados os nomes e valores do cliente mais alto, do mais baixo, do mais gordo e do mais magro, além
da média das alturas e dos pesos dos clientes
 
    >>> from secao_03_estrutura_de_repeticao import ex_37_senso_de_academia
    >>> lista_entradas = ['0', '81', '162', 'Renzo']  # Um aluno apenas
    >>> ex_37_senso_de_academia.input = lambda k: lista_entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Renzo, com 162 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Renzo, com 81 kilos
    Cliente mais gordo: Renzo, com 81 kilos
    --------------------------------------------------
    Media de altura dos clientes: 162.0 centímetros
    Media de peso dos clientes: 81.0 kilos
    >>> lista_entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante']
    >>> ex_37_senso_de_academia.input = lambda k: lista_entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Gigante, com 80 kilos
    Cliente mais gordo: Renzo, com 81 kilos
    --------------------------------------------------
    Media de altura dos clientes: 177.0 centímetros
    Media de peso dos clientes: 80.5 kilos
    >>> lista_entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante', '150', '170', 'Bolota']
    >>> ex_37_senso_de_academia.input = lambda k: lista_entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Gigante, com 80 kilos
    Cliente mais gordo: Bolota, com 150 kilos
    --------------------------------------------------
    Media de altura dos clientes: 174.7 centímetros
    Media de peso dos clientes: 103.7 kilos
    >>> lista_entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante', '150', '170', 'Bolota', '50', '172', 'Seco']
    >>> ex_37_senso_de_academia.input = lambda k: lista_entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Seco, com 50 kilos
    Cliente mais gordo: Bolota, com 150 kilos
    --------------------------------------------------
    Media de altura dos clientes: 174.0 centímetros
    Media de peso dos clientes: 90.2 kilos

"""

from operator  import itemgetter
from statistics import mean

def rodar_senso():
    """Escreva aqui em baixo a sua solução"""
    lista_de_alunos, lista_de_alturas, lista_de_pesos = [], [], []

    while True:
        aluno_nome = str(input('Informe o nome da pessoa ou digite "0" para finalizar o programa: '))
        if aluno_nome == '0':
            break
        else:
            aluno_altura = int(input('Digite a altura da pessoa: '))
            aluno_peso = int(input('Digite o peso da pessoa: '))
            lista_de_alunos.append([aluno_nome, aluno_altura, aluno_peso])

    o_mais_alto = max(lista_de_alunos, key=itemgetter(1))
    o_mais_baixo = min(lista_de_alunos, key=itemgetter(1))
    o_mais_gordo = max(lista_de_alunos, key=itemgetter(2))
    o_mais_magro = min(lista_de_alunos, key=itemgetter(2))
    # Declarando uma nova lista para armazenar apenas as alturas para achar a média (Mean)
    for i in range(len(lista_de_alunos)):
        lista_de_alturas.append(lista_de_alunos[i][1])
    altura_media = mean(lista_de_alturas)
    # Declarando uma nova lista para armazenar apenas os pesos para achar a média (Mean)
    for i in range(len(lista_de_alunos)):
        lista_de_pesos.append(lista_de_alunos[i][2])
    peso_medio = mean(lista_de_pesos)

    # Estava tentando usar executar o Sum e o Mean apenas no campo altura (ou peso)
    # utilizando o key=itemgetter mas não é possível.

    # altura_media = sum(lista_de_alunos, key=itemgetter(1)) / len(lista_de_alunos)
    # peso_medio = sum(lista_de_alunos, key=itemgetter(2)) / len(lista_de_alunos)
    # altura_media = mean(lista_de_alunos)
    # peso_medio = mean(key=itemgetter(2))

    altura_media2 = mean(lista_de_alunos, key=itemgetter(1))

    print(f'Cliente mais alto: {o_mais_alto[0]}, com {o_mais_alto[1]} centímetros')
    print(f'Cliente mais baixo: {o_mais_baixo[0]}, com {o_mais_baixo[1]} centímetros')
    print(f'Cliente mais magro: {o_mais_magro[0]}, com {o_mais_magro[2]} kilos')
    print(f'Cliente mais gordo: {o_mais_gordo[0]}, com {o_mais_gordo[2]} kilos')
    print(f'--------------------------------------------------')
    print(f'Media de altura dos clientes: {altura_media:.1f} centímetros')
    print(f'Media de peso dos clientes: {peso_medio:.1f} kilos')
    print(altura_media2)



