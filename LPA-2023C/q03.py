import os

# funções do programa
def escolha_servico() -> float:
    while True:
        # utilizando o scape \n para "pular" uma linha
        print('\nEntre com o tipo de serviço desejado')
        print('DIG - Digitalização')
        print('ICO - Impressão Colorida')
        print('IPB - Impressão Preto e Branco')
        print('FOT - Fotocópia')
        opcao = input('>>').upper()
        if (opcao == 'DIG'):
            return 1.10
        elif (opcao == 'ICO'):
            return 1.00
        elif (opcao == 'IBO'):
            return 0.40
        elif (opcao == 'FOT'):
            return 0.20
        else:
            print('Escolha Inválida.\nEntre com o tipo de serviço desejafo novamente.')

def num_pagina() -> float:
    while True:
        try:
            paginas = int(input('\nEntre com o número de páginas: '))
        except:
            print('Você digitou um valor inválido para o número de páginas')
            continue
        if paginas < 10:
            # forçando o retorno como um float
            return paginas * 1.0
        elif (paginas >= 10) and (paginas < 100):
            return paginas * (1 -0.10)
        elif (paginas >= 100) and (paginas < 1000):
            return paginas * (1 -0.15)
        elif (paginas >= 1000) and (paginas < 10000):
            return paginas * (1 -0.20)
        else:
            print('Não aceitamos tantas páginas de uma vez.')
            print('Por favor entre com o número de páginas novamente.')

def servico_extra() -> float:
    while True:
        print('\nDeseja adicionar mais algum serviço?')
        print('1 - Encadernação Simples - R$ 10,00')
        print('2 - Encadernação Capa Dura - R$ 25,00')
        print('0 - Não desejo mais nada')
        try:
            servico = int(input('>>'))
        except:
            # Vai selecionar o 'else:'
            servico = -1

        if (servico == 1):
            return 10.00
        elif (servico == 2):
            return 25.00
        elif (servico == 0):
            return 0
        else:
            print('Escolha Inválida.')
            print('Entre com o serviço desejado novamente.')

# Início do programa
# Limpar o console
os.system('cls') or None

print('Bem Vindo ao petshop do Fabiano Ferreira Mattoso')
servico = escolha_servico()
paginas = num_pagina()
extras = servico_extra()
total = servico * paginas + extras
# Usando o método format() para formatar os números com 2 casas
print('Total (R$): {0:.2f} (serviço: {1:.2f} * páginas: {2:.2f} + extra(s): {3:.2f})'.format(total, servico, paginas, extras))