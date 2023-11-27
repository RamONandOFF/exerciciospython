#Faça um programa que leia a largue e a altura de uma parede em metros.
# Calcule a sua área e a quantidade de tinta necessária para pinta-la sabendo
# que cada litro de tinta pinta uma área de 2m².

l = float(input('Qual a largura da parede? '))
a = float(input('Qual a altura da parede? '))

area = l * a

tinta = area / 2

print('A área total é de {:.2f}m². Sendo assim você vai precisar de {:.2f}L de tinta!'.format(area, tinta))
