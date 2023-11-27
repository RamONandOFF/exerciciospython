''' Crie um program que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maísculas e minúsculas
quantas letras ao todo ( sem considerar espaços).
quantas lertas tem o primeiro nome. '''

nome = str(input('Digite o seu nome: '))

print('Seu nome em maiúsculo é: {}.'.format(nome.upper()))
print('Seu nome em minúsculo é: {}.'.format(nome.lower()))
print('Seu nome tem ao todo {} caracteres.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} caracteres.'.format(nome.find(' ')))




