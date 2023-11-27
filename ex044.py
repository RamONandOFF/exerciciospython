'''Elabore um programa que calcule o valor a ser pago por um produto.
considerando o seu preço normal e condição de pagamento:
a vista dinheiro/cheque: 10% de desconto
a vista no cartao: 5% desconto
em até 2xno cartao : preço normal
3x ou mais no cartao: 20% de juros.'''

print('='*10,'LOJAS RIBEIRO','='*11)
p = float(input('Por favor digite o valor do produto R$: '))
m = int(input('''Selecione o método de pagamento!
[1] A vista (dinheiro/cheque).
[2] A vista no cartão.
[3] Em até 2x no cartão.
[4] Em 3x ou mais no cartão.'''))

if m == 1:
    print('O valor original de R${:.2f} com desconto para pagamento à vista ficará R${:.2f}.'.format(p, p-p*0.10))
elif m == 2:
    print('O valor original de R${:.2f} com desconto para pagamento à vista no cartão ficará R${:.2f}.'.format(p, p-p*0.05))
elif m == 3:
    print('O valor do produto em 2x no cartão ficará R${:.2f}.'.format(p))
elif m ==4:
    print('O valor do produto em 3x ou mais no cartão com juros terá seu valor final de R${:.2f}.'.format(p + (p*0.20)))
else:
    print('Opção inválida!! Por favor tente novamente.')
'''poderia ter colocado o valor da parcela e quanto ficaria o valor de cada parcela no código do programa
lembrar de fazer isso nos proximos programas , deixar bem mais completinho.'''



