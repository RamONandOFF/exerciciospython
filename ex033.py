'''Faça um programa que leia tres numeros e motre qual é o maior e qual é o menor.'''

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

l = [n1, n2, n3]

print('Entre os três números digitados, o maior número é: {}, e o menor número é {}.'.format(max(l), min(l)))
