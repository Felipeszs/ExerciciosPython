# Faça um programa que leia um número inteiro e mostre 
# na tela se é ou não um número primo.

numero = int(input('Digite um número: '))

for i in range(2, numero):
    if numero % i == 0:
        print(f'{numero} não é primo.')
        break # if
else:
    print(f'{numero} é primo.')

