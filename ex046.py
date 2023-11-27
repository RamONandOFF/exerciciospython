'''Faça um programa que mostre na tela uma contagem regressiva
para o estouro de fogos de artifício, indo de 10 até 0,
com uma pausa de 1 segundo entre eles.'''
import time

print('=-'*10)
input('Aperte ENTER para começar a contagem!!')


for c in range(10, -1, -1):
    print(c)
    time.sleep(1)# ou importando a biblioteca pode ser so sleep - from time import sleep
print(' KABUM! KABUUM!! KABUUUM!!!')
