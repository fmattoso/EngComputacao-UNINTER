"""
QUESTÃO 1 de 4 - Conteúdo até aula 03

Enunciado: Imagina-se que você é um dos programadores responsáveis pela construção de app de vendas para uma determinada empresa X que vende em atacado. Uma das estratégias de vendas dessa empresa X é dar desconto maiores conforme o valor da compra conforme a listagem abaixo:
· Se valor for menor que 1000 o desconto será de 0%;
· Se valor for igual ou maior que 1000 e menor que 3000 o desconto será de 3%;
· Se valor for igual ou maior que 3000 e menor que 5000 o desconto será de 5%;
· Se valor for igual ou maior que 5000 o desconto será de 8%;

Elabore um programa em Python que:

A. Deve-se implementar o print com uma mensagem de boas-vindas que apareça o seu nome [EXIGÊNCIA DE CÓDIGO 1 de 6];
B. Deve-se implementar o input do valor unitário e da quantidade do produto [EXIGÊNCIA DE CÓDIGO 2 de 6];
C. Deve-se implementar o desconto conforme a enunciado acima (obs.: atente-se as condições de menor, igual e maior) [EXIGÊNCIA DE CÓDIGO 3 de 6];
D. Deve-se implementar o valor total sem desconto e o valor total com desconto [EXIGÊNCIA DE CÓDIGO 4 de 6];
E. Deve-se implementar as estruturas if, elif e else (todas elas) [EXIGÊNCIA DE CÓDIGO 5 de 6];
F. Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 6 de 6];
G. Deve-se apresentar na saída de console uma mensagem de boas-vindas com seu nome [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 2];
H. Deve-se apresentar na saída de console um pedido recebendo desconto (valor total sem desconto acima de 1000 ) [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 2];

"""
import os

# Início do programa
# Limpar o console
os.system('cls') or None

print('Bem vindo a Loja do Fabiano Ferreira Mattoso')
valor_unitario = float(input('Entre com o valor do produto: '))
quantidade = float(input('Entre com a quantidade do produto: '))
valor_bruto = valor_unitario * quantidade
valor_desconto = valor_bruto
print('O valor SEM desconto: ', valor_bruto)

# Estrutura condicional if elif para definir a regra de cálculo
# optou-se por fazer 3% = 1 - 0.03 = 0.97 (por exemplo)
if (valor_bruto >= 1000) and (valor_bruto < 3000):
    valor_desconto = valor_bruto * (1 -0.03)
elif (valor_bruto >= 3000) and (valor_bruto < 5000):
    valor_desconto = valor_bruto * (1 -0.05)
elif (valor_bruto >= 5000):
    valor_desconto = valor_bruto * (1 -0.08)

# Saída do valor calculado. O scape '\n' vai incluir uma linha em branco
print('O valor COM desconto: ', valor_desconto, '\n')