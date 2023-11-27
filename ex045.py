'''Crie um programa que faça o computador jogar jokenpo com você'''
import random
import time

print('-='*20)
print('JO KEN PÔ')
print('-='*20)

o = int(input('''Digite uma opção:
[1] PEDRA.
[2] PAPEL.
[3] TESOURA.'''))

print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!')
time.sleep(1)

pc = random.randint(1, 3)

if o == 1 and pc == 1:
    print('Você escolheu PEDRA, eu TAMBÉM!- EMPATE!!')
elif o == 1 and pc == 2:
    print('Você escolheu PEDRA, eu PAPEL! - VOCÊ PERDEU!!')
elif o == 1 and pc == 3:
    print('Você escolheu PEDRA, eu TESOURA! - VOCÊ GANHOU!!')
elif o == 2 and pc == 1:
    print('Você escolheu PAPEL, eu PEDRA! - VOCÊ GANHOU!!')
elif o == 2 and pc == 2:
    print('Você escolheu PAPEL, eu TAMBÉM! - EMPATE!!')
elif o == 2 and pc == 3:
    print('Você escolheu PAPEL, eu TESOURA! - VOCÊ PERDEU!!')
elif o == 3 and pc == 1:
    print('Você escolheu TESOURA, eu PEDRA! - VOCÊ PERDEU!!')
elif o == 3 and pc == 2:
    print('Você escolheu TESOURA, eu PAPEL! - VOCÊ GANHOU!!')
elif o == 3 and pc == 3:
    print('Você escolheu TESOURA, eu TAMBÉM! -EMPATE!!')
