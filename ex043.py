'''desenvolva um programa que leia o peso e a altura de uma pessoa.
calcule seu imc e mostre seu status de acordo com a tabela abaixo:
abaixo de 18.5= abaixo do peso
entre 18.5 e 25= peso ideal
25 a 30: sobrepeso
30 até 40: obesidade
a cima de 40= obesidade morbida
'''
p = float(input('Digite o seu peso: '))
a = float(input('Digite a sua altura: '))

imc = p / (a**2)

if imc < 18.5:
    print('Seu IMC é de {:.2f}. Você está ABAIXO do peso!'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu IMC é de {:.2f}. Você está no peso IDEAL!!'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC é de {:.2f}. Você está com SOBREPESO!'.format(imc))
elif imc >= 30 and imc < 40:
    print('Seu IMC é de {:.2f}. Você está OBESO!'.format(imc))
else:
    print('Seu IMC é de {:.2f}. Obesidade mórbida! CUIDADO. Procure um MÉDICO!!'.format(imc))
