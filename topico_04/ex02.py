# Faça um programa que gere 10 números inteiros. 
# Em seguida, crie uma nova lista removendo os números
# repetidos. No final, mostre essa nova lista.
import random
<<<<<<< HEAD
lista_numeros = []
lista_semrepetidos = []
for i in range(10):
    lista_numeros.append(random.randint(1, 100))
    if lista_numeros[i] not in lista_semrepetidos:
        lista_semrepetidos.append(lista_numeros[i])

print(lista_numeros)
print(lista_semrepetidos)
=======

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
>>>>>>> 1c50802b07658cedb5ccde52674efa6de41d4c78
