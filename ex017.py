# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo,
# calcule e mostre o comprimento da hipotenusa.

from math import hypot

co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))

print('Sendo o cateto oposto de {} e o cateto adjacente {}, o comprimento da hipotenusa é de: {:.2f}; '. format(co, ca, hypot(co, ca)))
