'''Faça um programa que leia uma farse pelo teclado e mostre:
quantas vezes aparece a letra 'A'
em que posição ela aparece a primeira vez
em que posição ela aparece uma ultima vez.'''

n = str(input('Digite a frase por favor: ')).upper().strip()

print('A letra A aparece {} vezes na frase.'.format(n.count('A')))
print('A letra A aparece na posição {} pela primeira vez.'.format(n.find('A')+1))
print('A letra A aparece pela ultima vez na posição {}.' .format(n.rfind('A')+1))


