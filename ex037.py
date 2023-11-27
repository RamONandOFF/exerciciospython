n = int(input('Digite um número inteiro: '))

print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO)
[ 2 ] Converter para OCTAL)
[ 3 ] Converter para HEXADECIMAL)''')

op = int(input('Digite a sua opção: '))

if op == 1:
    print('O número {} em BINÁRIO é: {}.'.format(n, bin(n)[2:]))
elif op ==2:
    print('O número {} em OCTAL é: {}.'.format(n, oct(n)[2:]))
elif:
    print('O número {} em HEXADECIMAL é: {}.'.format(n, hex(n)[2:]))
else:
    print('Opão inválida. Tente novamente')



