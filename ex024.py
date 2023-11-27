# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
# tanto faz se é maisculo ou minusculo e não importa os espaços que tenham na frente.

cidade = str(input('Digite a cidade: ')).strip()

print(cidade[:5].upper() == 'SANTO')
