# Sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostra a ordem sorteada.
from random import shuffle

a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quartto aluno: ')

lista = [a1, a2, a3, a4]

shuffle(lista)

print('A ordem de apresentação do trabalho é: {}.'.format(lista))

