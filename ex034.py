'''Escreva um programa que pergunte o salário de um funcionario e
calcule o valor do seu aumento.
Para salários superiores a 1250, calcule um aumento de 10%
Para salários inferior ou iguais a 1250 o aumento é de 15%.'''

s = float(input('Digite o salário atual do funcionário em R$: '))
a1 = s + s * 0.10
a2 = s + s * 0.15

if s > 1250:
    print('O salário agora com aumento de 10% será de R${:.2f}.'.format(a1))
else:
    print('O salário agora com o aumento de 15% será de R${:.2f}.'.format(a2))
