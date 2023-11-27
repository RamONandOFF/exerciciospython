#crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome.

nome = str(input('Digite o seu nome por favor: ')).strip().lower().split()


print('Seu nome tem Silva? {}'.format('silva' in nome))