lista_livro = []
id_global = 0

def cadastrar_livro(id):
    print('*' * 80)
    print('{:-^80}'.format('MENU CADASTRAR LIVRO'))
    print('id do livro', id)
    nome = input('Por favor entre com o nome: ')
    autor = input('Por favor entre com o autor: ')
    editora = input('Por favor entre com a editora: ')

    dic_livro = {'id': id, 
                 'nome': nome,
                 'autor': autor,
                 'editora': editora}
    
    lista_livro.append(dic_livro)

def consular_livro():
    # Função aninhada para não repetir código desnecessariamente
    def print_resultado(lista):
        print('-' *40)
        for it in lista:
            for ch, vl in it.items():
                print(f"{ch}: {vl}")
        print('-' *40)

    # Início do corpo da função consultar_livro()
    print('*' * 80)
    while True:
        # usando format com código de formatação
        print('{:-^80}'.format('MENU CONSULTAR LIVRO'))
        print('Escolha a opção desejada:')
        print('1 - Consultar Todos os livros')
        print('2 - Colsultar Livro do id')
        print('3 - Consultar Livro(s) por autor')
        print('4 - Retornar')
        opcao = int(input('>>'))
        if opcao == 1:
            print_resultado(lista_livro)
        elif opcao == 2:
            id_pesquisa = int(input('Digite o id do livro: '))
            # Gerar uma lista, filtrando os IDs que correspondem ao valor de id_pesquisa
            filtro = [d for d in lista_livro if d["id"] == id_pesquisa]
            if filtro:
                print_resultado(filtro)
            else:
                print('id', id_pesquisa, 'não encontrado.')
        elif opcao == 3:
            autor_nome = input('Digite o autor do(s) livro(s): ')
            filtro = [d for d in lista_livro if str(d["autor"]).find(autor_nome) >= 0]
            if filtro:
                print_resultado(filtro)
            else:
                print('autor', autor_nome, 'não encontrado.')
        elif opcao == 4:
            return
        
def remover_livro():
    print('*' * 80)
    print('{:-^80}'.format('MENU REMOVER LIVRO'))
    try:
        id_remover = int(input('Digite o id do livro a ser removido: '))
        # Como a lista é "zero based", precisa decrementar 1 do id
        lista_livro.pop(id_remover -1)
    except:
        print('Não foi possível remover nenhum livro.')

print('Bem-vindo ao Controle de livros do Fabiano Ferreira Mattoso')
while True:
    print('*' * 80)
    print('{:-^80}'.format('MENU PRINCIPAL'))
    print('Escolha a opção desejada:')
    print('1 - Cadastrar Livro')
    print('2 - Colsultar Livro(s)')
    print('3 - Remover Livro')
    print('4 - Sair')
    opcao = int(input('>>'))

    if opcao == 1:
        id_global += 1
        cadastrar_livro(id_global)
    elif opcao == 2:
        consular_livro()
    elif opcao == 3:
        remover_livro()
    elif opcao == 4:
        break
    else:
        print('Opção inválida')
