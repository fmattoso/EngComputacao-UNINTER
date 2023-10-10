"""
QUESTÃO 2 de 4 - Conteúdo até aula 04

Enunciado: Você e sua equipe de programadores foram contratados para desenvolver um app de vendas para uma loja que vende Açaí e Cupuaçu. Você ficou com a parte de desenvolver a interface do cliente para retirada do produto.
A Loja possui seguinte relação:
· Tamanho P de Cupuaçu (CP) custa 10 reais e o Açaí (AC) custa 12 reais;
· Tamanho M de Cupuaçu (CP) custa 15 reais e o Açaí (AC) custa 17 reais;
· Tamanho G de Cupuaçu (CP) custa 19 reais e o Açaí (AC) custa 21 reais;

Elabore um programa em Python que:
A. Deve-se implementar o print com uma mensagem de boas-vindas que apareça o seu nome [EXIGÊNCIA DE CÓDIGO 1 de 8];
B. Deve-se implementar o input do sabor (CP/AC) e o print “Sabor inválido. Tente novamente" se o usuário entra com valor diferente de CP e AC [EXIGÊNCIA DE CÓDIGO 2 de 8];
C. Deve-se implementar o input do tamanho (P/M/G) e o print “Tamanho inválido. Tente novamente" se o usuário com entra valor diferente de P,M ou G [EXIGÊNCIA DE CÓDIGO 3 de 8];
D. Deve-se implementar if/elif com cada uma das combinações de sabor e tamanho do enunciado [EXIGÊNCIA DE CÓDIGO 4 de 8];
E. Deve-se implementar um acumulador para somar os valores dos pedidos [EXIGÊNCIA DE CÓDIGO 5 de 8];
F. Deve-se implementar o input com a pergunta: “Deseja pedir mais alguma coisa?”. Se sim repetir a partir do item B, senão encerrar o programa executar o print do acumulador [EXIGÊNCIA DE CÓDIGO 6 de 8];
G. Deve-se implementar as estruturas de while, break, continue (todas elas) [EXIGÊNCIA DE CÓDIGO 7 de 8];
H. Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 8 de 8];
I. Deve-se apresentar na saída de console uma mensagem de boas-vindas com o seu nome [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 4];
J. Deve-se apresentar na saída de console um pedido em que o usuário errou o sabor [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 4];
K. Deve-se apresentar na saída de console um pedido em que o usuário errou o tamanho [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 4];
L. Deve-se apresentar na saída de console um pedido com duas opções sabores diferentes e com tamanhos diferentes [EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 4];
"""

import os

# Início do programa
# Limpar o console
os.system('cls') or None

valor_total = 0
valor_item = 0
print('Bem vindo a Loja do Fabiano Ferreira Mattoso')
print('-' *30, 'Cardápio', '-' *30)
print('-' *6, '| Tamanho | Cupuaçu (CP) | Açaí (AC) |', '-' *6)
print('-' *6, '|    P    |   R$ 10,00   |  R$ 12,00 |', '-' *6)
print('-' *6, '|    M    |   R$ 15,00   |  R$ 17,00 |', '-' *6)
print('-' *6, '|    G    |   R$ 19,00   |  R$ 21,00 |', '-' *6)
print('-' * 60)
while True:
    sabor = input('Entre com o sabor desejado (CP/AC): ')
    if (sabor.upper() == 'CP'):
        nome_sabor = 'CUPUAÇU'
    elif (sabor.upper() == 'AC'):
        nome_sabor = 'AÇAÍ'
    else:
        print('Sabor Inválido. Tente novamente')
        continue

    tamanho = input('\nEntre com o tamanho desejado (P/M/G): ')
    if (tamanho.upper() == 'P'):
        if (sabor.upper() == 'CP'):
            valor_item = 10
        else:
            valor_item = 12
    elif (tamanho.upper() == 'M'):
        if (sabor.upper() == 'CP'):
            valor_item = 15
        else:
            valor_item = 17
    elif (tamanho.upper() == 'G'):
        if (sabor.upper() == 'CP'):
            valor_item = 19
        else:
            valor_item = 21        
    else:
        print('Tamanho inválido. Tente novamente')
        continue

    print('Você pediu ', nome_sabor, ' no tamanho ', tamanho.upper(), ': R$ ', valor_item)
    valor_total += valor_item
    continua = input('Deseja mais alguma coisa (s/digite outra tecla)?: ')
    if (continua.lower() != 's'):
        break

print('\nO valor total a ser pago: R$ ', valor_total)
