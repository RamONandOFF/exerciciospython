r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas PODEM formar um triangulo.')
    if r1 == r2 == r3:
        print('Este tipo de triângulo é chamado de Equilátero.')
    elif r1 != r2 != r3 != r1:
        print('Este tipo de triângulo é chamado de Escaleno.')
    else:
        print('Este tipo de triângulo é chamado de Isósceles ')
else:
    print('As retas NÃO PODEM formar um triangulo.')
