'''Escreva um programa para aprovar o empréstimo bancário para a
compra de uma casa. Pergunte o :
valor da casa
salário do comprador
em quantos anos irá pagar.
A prestação mensal não pode exceder 30% do salário ou entao o emprestimo sera negado!!'''

c = float(input('Digite o valor da casa: '))
s = float(input('Digite o seu salário atual: '))
t = int(input('Digite o tempo em anos que deseja pagar: '))

emp = c/(t*12)

if emp <= s*0.30:
    print('Para pagar uma casa de R${:.2f} em {} anos , a prestação será de R${:.2f}!\nEmpréstimo pode ser CONCEDIDO!'.format(c, t, emp))
else:
    print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}!\nEmpréstimo NEGADO!!'.format(c, t, emp))





