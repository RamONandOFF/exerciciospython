'''A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria de acordo com sua idade:
até 09 anos: mirim
até 14: infantil
até 19: junior
até 25 : senior
acima: master'''

from datetime import date

at = int(input('Digite a data de nascimento do atleta: '))

idade = date.today().year - at

if idade <= 9:
    print('O atleta tem {} anos e corresponde à categoria MIRIM.'.format(idade))
elif idade <= 14:
    print('O atleta tem {} anos e corresponde à categoria INFANTIL.'.format(idade))
elif idade <= 19:
    print('O atleta tem {} anos e corresponde à categoria JUNIOR.'.format(idade))
elif idade <= 25:
    print('O atleta tem {} anos e corresponde à categoria SÊNIOR.'.format(idade))
else:
    print('O atleta tem {} anos e corresponde à categoria MASTER.'.format(idade))

'''from datetime import date
date.today().year
isso faz com que pegue o '''