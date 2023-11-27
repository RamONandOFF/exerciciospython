#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

s = float(input('Digite o salário do funcionário. R$: '))

a = s * 0.15

print('O salário de R${:.2f} com o aumento de 15% passará a ser de R${:.2f}.'.format(s, (s+a)))

