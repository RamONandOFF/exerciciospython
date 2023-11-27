'''Faça um programa que leia o ano de nascimento de um jovem e informe:
de acordo com sua idade se ele:
ainda vai se alistar ao serviço militar
se é a hora de se alistar
ou se já passou do tempo do alistament
Seu programa também deverá mostrar o tempo que faltou ou que passou do prazo.'''

ano = int(input('Digite o ano de seu nascimento: '))
al = 2023 - ano

if al > 18:
    print('Você tem {} anos e já passou da idade do alistamento!'.format(al))
elif al == 18:
    print('Você completou ou irá completar {} anos este ano!\n'
          '!!!!ALISTE-SE IMEDIATAMENTE!!!!'.format(al))
else:
    print('Você tem {} anos, ainda é muito novo para o serviço militar!'.format(al))


