# Faça um programa em que ele sorteie um número entre 0 e 5. 
# O usuário deverá então adivinhar este número e o programa
# deverá escrever na tela se ele acertou ou não.
import random

sorteio = random.randint(0, 5)

numero = int(input('Digite um número: '))

if numero == sorteio:
    print('Você acertou!')
else:
    print(f'Você errou, o número era {sorteio}.')