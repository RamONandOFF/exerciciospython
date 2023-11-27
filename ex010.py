# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos dólares ela pode comprar.
# considerando o dólar atual de = 4,77

m = float(input('Para a conversão em U$$, digite o valor em R$: '))

d = m / 4.77

print('O valor digitado de R$ {} pode comprar um total de U$$ {:.2f}. Boas compras!'.format(m, d))
