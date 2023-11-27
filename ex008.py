#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = float(input('Digite o valor em metros para conversão: '))

c = m*100
mm = m*1000

print('O valor de {}m é igual a {:.0f}cm e {:.0f}mm.'.format(m, c, mm))

