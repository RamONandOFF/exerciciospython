'''desenvolva um programa que leia seis numeros inteiros
e mostre a soma apena daqueles que forem pares.
se o valor digitado for impar, desconsidere-o'''

soma = 0
cont = 0

for c in range(1, 7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} números PARES e a soma deles foi {}'.format(cont, soma))

