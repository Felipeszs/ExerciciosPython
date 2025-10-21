# Faça um programa que gere 10 números inteiros. 
# Em seguida, crie uma nova lista removendo os números
# repetidos. No final, mostre essa nova lista.
import random

lista = []
for i in range(10):
    lista.append(random.randint(0, 10))

# x = random.sample(range(0, 10), 5)
# y = random.sample(range(0, 10), 5)
# x += y 

print(lista)

lista_sem_repeticoes = []
for elemento in lista:
    if elemento not in lista_sem_repeticoes:
        lista_sem_repeticoes.append(elemento)

print(lista_sem_repeticoes)