"""
Exercício 41 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida,
valor dos juros, quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1                                0
3                                10
6                                15
9                                20
12                               25

    >>> gerar_dados_de_financiamente(1000)
    Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
    R$ 1000.00      0%              1                       R$   1000.00
    R$ 1100.00      10%             3                       R$    366.67
    R$ 1150.00      15%             6                       R$    191.67
    R$ 1200.00      20%             9                       R$    133.33
    R$ 1250.00      25%             12                      R$    104.17
    >>> gerar_dados_de_financiamente(1500)
    Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
    R$ 1500.00      0%              1                       R$   1500.00
    R$ 1650.00      10%             3                       R$    550.00
    R$ 1725.00      15%             6                       R$    287.50
    R$ 1800.00      20%             9                       R$    200.00
    R$ 1875.00      25%             12                      R$    156.25

"""


def gerar_dados_de_financiamente(valor_inicial: float):
    """Escreva aqui em baixo a sua solução"""
    divida_10 = valor_inicial * 1.1
    divida_15 = valor_inicial * 1.15
    divida_20 = valor_inicial * 1.2
    divida_25 = valor_inicial * 1.25

    valor_da_parcela_3 = divida_10 / 3
    valor_da_parcela_6 = divida_15 / 6
    valor_da_parcela_9 = divida_20 / 9
    valor_da_parcela_12 = divida_25 / 12

    nova_entrada = [(valor_inicial, '0%', '1', valor_inicial),
                    (divida_10, '10%', '3', valor_da_parcela_3),
                    (divida_15, '15%', '6', valor_da_parcela_6),
                    (divida_20, '20%', '9', valor_da_parcela_9),
                    (divida_25, '25%', '12', valor_da_parcela_12)]


    print("{:<2} {:<1} {:<1}  {:<1}".format('Valor da Dívida', 'Valor dos Juros', 'Quantidade de Parcelas', 'Valor da Parcela'))


    for n in nova_entrada:
        divida, porcentagem, qtde_parcelas, valor_parcelas = n
        print("R$ {:<12.2f} {:<15} {:<23} R${:>10.2f}".format(divida, porcentagem, qtde_parcelas, valor_parcelas))
