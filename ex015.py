# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado,
# a quantidade de dias pelos quais ele foi alugado e calcule o preço a pagar,
# sabendo que o carro custa 60 por dia e 0.15 por km rodado.

km = float(input('Quantos Km o veículo percorreu? '))
dia = int(input('Quantos dias o veículo ficou alugado? '))

pag = km * 0.15 + 60 * dia

print('O veículo rodou {:.2f}Km, e ficou {} dias alugado, sendo assim o valor final é de R${:.2f}.'.format(km, dia, pag))
