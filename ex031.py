'''Desenvolva um progrmaa que pergunte a distancia de uma viagem em KM.
Calcule o preço da passagem, cobrando 0.50 por km
para cada viagen de até 200km e 0.45 para viagens mais longas'''

v = int(input('Digite a distância da viagem em KM: '))

if v <= 200:
    p = v * 0.50
    print('O valor da sua passagem é de R${:.2f}.'.format(p))
else:
    p = v * 0.45
    print('O valor da sua passagem é de R${:.2f}.'.format(p))
