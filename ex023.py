#Faça um progrmaa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
# EX: digite um numero  1834
# Unidade : 4, dezena, 3, centena 8 milhar :1

num = int(input('Informa um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analisando o número {}...'.format(num))
print('Unidade: {}.'.format(u))
print('Dezena: {}.'.format(d))
print('Centena: {}. '.format(c))
print('Milhar: {}.'.format(m))
