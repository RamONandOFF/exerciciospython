'''Crie um progrmaa que leia duas notas de um aluno e calcule sua média.
Mostre uma mensagem no final de acordo com a média atingida:
a baixo de 5.0 = reprovado
entre 5.0 e 6.9= em recuperação
7.0 + = aprovado.
10= mensagme de felicitação'''

n1= float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1+n2) / 2

if m < 5:
    print('Sua média foi de {}. REPROVADO!!'.format(m))
elif m >= 5 and m < 7:
    print('Sua média foi de {}.\nVocê está de RECUPERAÇÃO!'.format(m))
elif m >= 7 and m < 10:
    print('Sua média foi de {}. Parabéns! Você está APROVADO!!'.format(m))
elif m == 10:
    print('Sua média foi de {}. \n!!VOCÊ É INCRÍVEL!!\n!!!SUPER APROVADO!!!'.format(m))
