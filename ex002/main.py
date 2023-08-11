#Tela de Bem-vindo: Como na aula de apoio vi que poderia 'customizar' a tela de bem-vindo, mudei a cor.

print('{}É um Prazer Recebe-lo na Sorveteria Adrian Moizes do Nascimento Alves:{}' .format('\033[1;30;44m', '\033[m'))

print('{}--------------------------------------CARDÁPIO-------------------------------------{}' .format('\033[0;34m', '\033[m'))

print('{}| Nº de Bolas | Sabor Tradicional (tr) | Sabor Premium (pr) | Sabor Especial (es) |{}' .format('\033[4;34m', '\033[m'))

print(f'\033[4;34m|{1:>8}     |    {6:>9,.2f}           |  {7:10,.2f}        | {8:>11,.2f}         |\033[m')

print(f'\033[4;34m|{2:>8}     |    {11:>9,.2f}           |  {13:10,.2f}        | {15:>11,.2f}         |\033[m')

print(f'\033[4;34m|{3:>8}     |    {15:>9,.2f}           |  {18:10,.2f}        | {21:>11,.2f}         |\033[m')

print('') #pular linha, deixa o código mais organizado.

bola = 0

# Loop While que recebe os sabores e quantidade de bolas desejados:

while True:

    sabor = input('Escolha um tipo de sabor (tr/pr/es): ')

    if sabor != 'tr' and sabor != 'es' and sabor != 'pr':

        print('Sabor Inválido. Tente novamente digitando um sabor existente.')

        continue  # teste para saber se o valor digitado de SABOR é verdadeiro, caso não seja, ele retornará o loop.

    num_bolas = (input('Escolha o número de bolas (1/2/3): '))

    if num_bolas != '1' and num_bolas != '2' and num_bolas != '3':

        print('Número Inválido. Tente novamente digitando um número existente.')

        continue  # teste para saber se o valor digitado NUM_BOLAS é verdadeiro, caso não seja, ele retornará o loop.

    # SABORES TRADICIONAIS

    if sabor == 'tr' and num_bolas == '1' or '2' or '3':

        if num_bolas == '1' and sabor != 'es' and sabor != 'pr':

            print('Voce pediu 1 bola de sorvete no sabor TRADICIONAL: R$6.00')

            bola += 6.00

        elif num_bolas == '2' and sabor != 'es' and sabor != 'pr':

            print('Voce pediu 2 bolas de sorvete no sabor TRADICIONAL: R$11.00')

            bola += 11.00

        elif num_bolas == '3' and sabor != 'es' and sabor != 'pr':

            print('Voce pediu 3 bolas de sorvete no sabor TRADICIONAL: R$15.00')

            bola += 15.00

            # SABORES PREMIUM

    if sabor == 'pr' and num_bolas == '1' or '2' or '3':

        if num_bolas == '1' and sabor != 'es' and sabor != 'tr':

            print('Voce pediu 1 bola de sorvete no sabor PREMIUM: R$7.00')

            bola += 7.00

        elif num_bolas == '2' and sabor != 'es' and sabor != 'tr':

            print('Voce pediu 2 bolas de sorvete no sabor PREMIUM: R$13.00')

            bola += 13.00

        elif num_bolas == '3' and sabor != 'es' and sabor != 'tr':

            print('Voce pediu 3 bolas de sorvete no sabor PREMIUM: R$18.00')

            bola += 18.00

            # SABORES ESPECIAIS

    if sabor == 'es' and num_bolas == '1' or '2' or '3':

        if num_bolas == '1' and sabor != 'tr' and sabor != 'pr':

            print('Voce pediu 1 bola de sorvete no sabor ESPECIAL: R$8.00')

            bola += 8.00

        elif num_bolas == '2' and sabor != 'tr' and sabor != 'pr':

            print('Voce pediu 2 bolas de sorvete no sabor ESPECIAL: R$15.00')

            bola += 15.00

        elif num_bolas == '3' and sabor != 'tr' and sabor != 'pr':

            print('Voce pediu 3 bolas de sorvete no sabor ESPECIAL: R$21.00')

            bola += 21.00

            # Aqui o algoritmo apresenta a escolha se o loop termina, ou continua para escolher um novo tipo de sorvete.

    sair = input('Deseja comprar mais algum sorvete? se SIM, aperte (s). Se NÃO, aperte qualquer outra tecla e dê ENTER. ')

    if sair:

        if sair != 's':

            break

        else:

            continue

print('')  # pular linha, deixa o código mais organizado.

print('O valor total a ser pago: R${:.2f}'.format(bola))