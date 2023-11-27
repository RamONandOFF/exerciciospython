'''Escreve um progrmaa que leia dois numeros inteiros
compare-os e mostre na tela uma mensagem:
o primeiro valor é maior
o segundo valor é maior
não existe valor maior, os dois são iguais'''

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('Entre {} e {} o maior número é: {}.'.format(n1, n2, n1))
elif n1 < n2:
    print('Entre {} e {} o maior número é: {}.'.format(n1,n2,n2))
else:
    print('Os números sãos iguais!')
