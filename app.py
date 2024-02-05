import os

restaurantes = [{'nome': 'oficina', 'categoria':'lanchonete', 'ativo':False},
                {'nome': 'chiquerrimo', 'categoria':'chique', 'ativo':True},
                {'nome': 'ierri', 'categoria':'nordestino', 'ativo':False}]

def exibir_name():
    '''exibi o titulo do app'''

    print("""
𝓸𝓯𝓲𝓬𝓲𝓷𝓪 𝓭𝓸 𝓵𝓪𝓷𝓬𝓱𝓮
          """)

def exibir_op():
    '''lista as opções de funcionalidades'''
    print("1. cadastrar restaurante")
    print("2. listar restaurantes")
    print("3. ativar restaurante")
    print("4. sair")

def finalizar_app():
    '''finaliza o programa limpando o console'''
    exibir_subtitulos('finalizando o programa')

def voltar_menu():
    '''exibe a menssagem de encerramento 


    outputs:
    retorna ao menu principal do programa
    
    inputs:
    -pressionar enter e voltar

    '''
    input('\npressione enter para voltar ao menu')
    os.system('cls')
    main()

def op_invalida():
    '''mostra a menssagem de inavaliudo 
    
    outputs:
    retorna ao menu principal
    
    '''
    print('opção invalida\n')
    voltar_menu()

def exibir_subtitulos(texto):
    '''exibe todos os subtitulos
    
    Inputs:
    - texto: str - O texto do subtítulo
    '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)

def cadastro():
    '''realiza o cadastro de novos restaurantes
    inputs:
    -nome do restaurante
    -categoria

    outputs:
    - Adiciona um novo restaurante à lista de restaurantes

    '''
    exibir_subtitulos('cadastro de novos restaurantes')
    name_res = input('degite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'digite a categoria do restaurante {name_res}: ')
    dados_rest = {'nome': name_res, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_rest)
    print(f'o restaurante {name_res} foi cadastrado com sucesso!\n')
    voltar_menu()

def ativar_restaurante():
    '''altera o estado do restaurante
    
    inputs:
    -nome do restaurante pra ativar ou desativar

    output:
    -altera da lista de ativo para desativado e vise versa

    '''
    exibir_subtitulos('arternando ou ativando o estado do restaurante')
    nome_restaurante = input('digite o nome do restarante que deseja ativar ou desativar: ')
    resrante_encon = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            resrante_encon = True
            restaurante['ativo'] = not restaurante['ativo']
            menssagem = f'O restaurante {nome_restaurante} foi ativado' if restaurante['ativo'] else f'O restaurante foi desativado'
            print(menssagem)
    if not resrante_encon:
        print('O restaurante não foi encontrado')
    

def listar_restaurante():
    '''lista os restaurantes na lista

    outputs:
    exibe a lista dos restaurantes cadastrados'''
    exibir_subtitulos('listar restaurantes')

    print(f"{'Nome do restaurante'.ljust(22)}   {'Categoria'.ljust(20)}   Status")
    for restaurante in restaurantes:
        name_rest = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {name_rest.ljust(20)} | {categoria.ljust(20) } | {ativo}')
        
    voltar_menu()

def escolher_op():
    '''escolher as opções de funcionalidades
    outputs:
    -executa a opção escolhida

    '''
    try:
        opcao_escolhida = int(input('escolha uma opção '))

   
        if opcao_escolhida == 1:
            cadastro()
        elif opcao_escolhida == 2:
            listar_restaurante()
        elif opcao_escolhida == 3:
            ativar_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            op_invalida()
    except:
        op_invalida()

def main():
    '''menu principal'''
    os.system('cls')
    exibir_name()
    exibir_op()
    escolher_op()

if __name__ == '__main__':
    main()
