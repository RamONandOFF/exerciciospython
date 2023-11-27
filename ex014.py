# Escreva um programa que converta uma temperatura digita em ªC e converta para ªF.

c = float(input('Digite a temperatura em ªC: '))

f = c * 9/5 + 32

print('A temperatura de {:.2f}ªC corresponde a exatamente {:.2f}ªF.'.format(c, f))