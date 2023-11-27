'''Escreve um programa que faça o computador 'pensar' em um numero
inteiro entre 0 e 5 e peça para o usuario tentar descobrir qual foi
o numero escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

import random
import time

n = int(input('Digite um número de 0 a 5: '))
s = random.randint(0, 5)

print('Processando, aguarde...')

time.sleep(3)

if s == n:
    print('O número sorteado foi {}. Parabéns você acertou!'.format(s))
else:
    print('O número sorteado foi {}. Que pena, você errou!'.format(s))

