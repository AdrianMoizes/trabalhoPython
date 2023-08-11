print('Seja bem-vindo ao Atacadão, Adrian Moizes do Nascimento Alves!')
print('Cupons Válidos')
# Esses print são apenas para deixar mais apresentável para o cliente sobre os cupons que estão aplicáveis, isso
# acaba incentivando-os a comprarem mais.
print(' 5% em compras a partir de: 200 unidades.')
print(' 10% em compras a partir de: 1000 unidades.')
print(' 15% em compras a partir de: 2000 unidades.')

# Inputs para armazenar os valores dos produtos e as suas quantidades.
valor_produto = float(input('informe o valor do produto: '))
valor_quantidade = int(input('informe a quantidade dos produtos: '))
valor_total = valor_produto * valor_quantidade

# Esse algoritmo armazena na variável "desconto" o valor, em real, do desconto a ser aplicado
# nas compras acima de 200 unidades. O print pega esse valor armazenado na variável e subtrai do valor total.
if valor_total > 0:
    print('O valor SEM desconto: R$ {}'.format(valor_total))
    if valor_quantidade < 200:
        print('O valor COM desconto: R$ {}'.format(valor_total))
    elif valor_quantidade >= 200 and valor_quantidade < 1000:
        desconto = 5 * valor_total / 100
        print('O valor COM desconto: R$ {}'.format(valor_total - desconto))
    elif valor_quantidade >= 1000 and valor_quantidade < 2000:
        desconto = 10 * valor_total / 100
        print('O valor COM desconto: R$ {}'.format(valor_total - desconto))
    else:
        desconto = 15 * valor_total / 100
        print('O valor COM desconto: R$ {}'.format(valor_total - desconto))
else:
    print('Informe um valor e quantidade válida. ')
#NOTA: tentei ser o mais original possível dentro do que foi preestabelecido, e gostei do resultado. .
