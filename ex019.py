#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um progrmaa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
from random import choice

a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')

list = a1, a2, a3, a4

print('O aluno escolhido para apagar o quadro é: {}. Parabéns!'.format(choice(list)))
