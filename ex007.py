#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda note: '))

m = (n1+n2)/2

print("Com base em sua primeira nota de {} e sua segunda nota de {}, a sua média final é de {}.".format(n1, n2, m))
