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
