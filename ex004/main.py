#ex04:
 #lista que armazena os colaboradores cadastrados.
lista_colaboradores = []
 #variável com o id dos colaboradores.
id_global = 0

 #função cadastrar colaborador.
def cadastrar_colaborador(id_global):
    print('\033[34m' + '____________________________MENU CADASTRAR COLABORADOR_________________________' + '\033[0m')
    print('Código do Colaborador {}' .format(id_global))
    nome = input('Digite o nome do colaborador: ')
    setor = input('Digite o nome do setor do colaborador: ')
    pgt = input('Digite o pagamento do colaborador (R$): ')
    dicionario = {'Código':id_global,'Nome':nome,'Setor':setor,'Pagamento':pgt} #dicionário que armazena as variáveis e acrecenta um id em forma de string.
    lista_colaboradores.append(dicionario.copy()) #lista que faz uma cópia do dicionário.

 #função consultar colaborador.
def consultar_colaborador():
    while True:
        print('\033[34m' + '___________________________MENU CONSULTAR COLABORADOR___________________________' + '\033[0m')
        consul = input('ESCOLHA A OPÇÃO DESEJADA:\n '
                               + '1-Consultar Todos\n '
                               + '2-Consultar por ID\n '
                               + '3-Consultar por Setor\n '
                               + '4-Retornar ao Menu\n'
                               + '>>:')
        if consul == '1':
            for produto in lista_colaboradores: #Crei uma variável 'produto' que virou um dicionário e interei dentro da lista.
                print('______________________')
                for i, j in produto.items(): #Aqui foram criadas mais duas variáveis 'i e j' para interar no 'produto', criado anteriormente.
                    print('{}: {}' .format(i, j))
        elif consul == '2':
            valor = int(input('Digite o ID do Colaborador: ')) #tranformei o input em int porque todo id deve ser inteiro.
            for produto in lista_colaboradores:
                if produto['Código'] == valor:
                    print('______________________')
                    for i, j in produto.items():  # Aqui foram criadas mais duas variáveis 'i e j' para interar no 'produto', criado anteriormente.
                        print('{}: {}'.format(i, j))
                    print('______________________')
        elif consul == '3':
            valor = input('Digite o Setor do Colaborador: ')
            for produto in lista_colaboradores:
                if produto['Setor'] == valor:
                    print('______________________')
                    for i, j in produto.items():  # Aqui foram criadas mais duas variáveis 'i e j' para interar no 'produto', criado anteriormente.
                        print('{}: {}'.format(i, j))
                    print('______________________')
        elif consul == '4':
            print('Voltando ao Menu...')
            return
        else:
            print('Opção Inválida. Entre com(1/2/3/4)') #caso a opção digitada seja inválida, retorna o laço

 #função remover colaborador
def remover_colaborador():
    print('\033[34m' + '____________________________MENU REMOVER COLABORADOR____________________________' + '\033[0m')
    valor = int(input('Digite o ID do Colaborador para remover: '))  #tranformei o input em int porque todo id deve ser inteiro.
    for produto in lista_colaboradores:
        if produto['Código'] == valor:
            lista_colaboradores.remove(produto) #remove o colaborador que é representado pelo ID digitado.
            print('Colaborador Removido com Sucesso!\n'+'______________________')

 #código principal:
print('\033[34m' + '------->SEJAM BEM-VINDOS AO CONTROLE DE COLABORADORES DO ADRIAN ALVES!<---------\n' + '*' * 80 + '\033[0m')
while True:
    print('\033[34m' + '_________________________________MENU PRINCIPAL_________________________________' + '\033[0m\n')
    menu_principal = input('ESCOLHA A OPÇÃO DESEJADA:\n '
                           + '1-Cadastrar Colaborador\n '
                           + '2-Consultar Colaborador(es)\n '
                           + '3-Remover Colaborador\n '
                           + '4-Encerrar Programa\n'
                           + '>>:')
    if menu_principal == '1':
        id_global += 1 #acrescenta um id a cada novo cadastro
        cadastrar_colaborador(id_global)
    elif menu_principal == '2':
        consultar_colaborador()
    elif menu_principal == '3':
        remover_colaborador()
    elif menu_principal == '4':
        print('Encerrando o Programa...')
        break
    else:
        print('Opção Inválida. Entre com(1/2/3/4)') #caso a opção digitada seja inválida, retorna o laço