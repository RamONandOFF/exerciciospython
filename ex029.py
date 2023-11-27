'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h. mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7,00 por cada Km acima do limite'''

v = float(input('Insira a velociade do carro: '))

if v > 80:
    m = (v-80)*7
    print('VAI COM CALMA! Você recebeu uma multa de R${} por ser apressadinho!'.format(m))
else:
    print('PARABÉNS! Você esta dirigindo numa velocidade adequada!')

