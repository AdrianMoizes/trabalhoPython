# função para solicitar o peso do cachorro.

def cachorro_peso():
    while True:

        peso = input('Entre com o peso do cachorro: ')

        try:  # tentará execultar a linha de código.

            if 0 < int(peso) < 3:

                valor = 40

            elif 3 <= int(peso) < 10:

                valor = 50

            elif 10 <= int(peso) < 30:

                valor = 60

            elif 30 <= int(peso) < 50:

                valor = 70

            else:

                int(peso) > 50

                print('Não atendemos cachorros desse porte.')

                continue

            return valor

        except ValueError:  # para um valor fora do padrão recebido. Ex: letras ou decimais.

            print('Digite um Valor Inteiro.')

        # função para solicitar o pelo do cachorro.


def cachorro_pelo():
    while True:

        pelo = input(
            'Entre com o tamanho do pelo do cachorro: \n' + 'c - Pelo curto.\n' + 'm - Pelo médio.\n' + 'g - Pelo grande.\n ' + '>>:')

        pelo = pelo.lower()  # deixar o input sempre em caixa baixa.

        pelo = pelo.strip()  # ignora espacos dogitados no teclado.

        if pelo == 'c':

            mult = valor * 1

        elif pelo == 'm':

            mult = valor * 1.5

        elif pelo == 'g':

            mult = valor * 2

        else:

            print('Digite um valor válido(c/m/g) ')

            continue

        return mult

        # este código retorna o peso já com o multiplicador.


# função para solicitar algum adicional.

def cachorro_extra():
    total = 0  # acumula os adicionais toda vez que acontece um loop.

    while True:

        adc = input(
            'Deseja adicionar mais Algum serviço? \n' + 'Cortar as unhas:____(1) - R$10,00\n' + 'Escovar os dentes:__(2) - R$12,00\n' + 'Limpar as orelhas:__(3) - R$15,00\n' + 'Não desejo mais nada:__(0)\n' + '>>:')

        if adc == '0':

            return total

        elif adc == '1':

            total += 10

            continue

        elif adc == '2':

            total += 12

            continue

        elif adc == '3':

            total += 15

            continue

        else:

            print('Digite um valor válido(0/1/2/3) ')

        continue

    # Conteúdo principal:


print('{}PetShop, Adrian Moizes do Nascimento Alves, “Pelos melhores preços em produtos para pets!(>.<)”{}'.format(
    '\033[1;30;44m', '\033[m'))

valor = cachorro_peso()

opcao = cachorro_pelo()

total = cachorro_extra()

print('Total a pagar: R${},00 (Peso * Pelo: R${},00 + adicional(is): R${},00)'.format(opcao + total, opcao, total))