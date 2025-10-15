# Faça um programa que gere 10 números inteiros. 
# Em seguida, crie uma nova lista removendo os números
# repetidos. No final, mostre essa nova lista.
import random
lista_numeros = []
lista_semrepetidos = []
for i in range(10):
    lista_numeros.append(random.randint(1, 100))
    if lista_numeros[i] not in lista_semrepetidos:
        lista_semrepetidos.append(lista_numeros[i])

print(lista_numeros)
print(lista_semrepetidos)
