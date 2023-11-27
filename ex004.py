#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e
# todas as informações possívels sobre ele.

algo = (input('Digite algo: '))

print('Só tem espaços?', algo.isspace())
print('É um número?', algo.isnumeric())
print('É alfabético?', algo.isalpha())
print('É alfanumérico?', algo.isalnum())
print('Está em maiúscula? ', algo.isupper())
print('Está em minúsculas?', algo.islower())
print('Está capitalizada?', algo.istitle())


