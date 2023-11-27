#Faca um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo
import math
from math import cos, sin, tan, radians

a = float(input('Insira um ângulo qualquer: '))

s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))

print('O ângulo {:.2f}, tem o seno de {:.2f}, cosseno de {:.2f} e tangente de {:.2f}.'.format(a, s, c, t))
