# faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

p = float(input('Qual o preço do produto? R$: '))

d = p * 0.05

print('O produto no valor de R$:{:.2f}, com 5% de desconto terá o novo preço de R${:.2f}.'.format(p, (p-d)))
