# Dada uma lista de números inteiros, 
# imprima todos os elementos distintos.

numeros = [1, 2, 3, 3, 4, 5]

print(list(set(numeros)))

# numeros_str = numeros.map(lambda x: str(x))

# numeros_str = [str(numero) for numero in numeros]

# numeros_str = []
# for numero in numeros:
#     numeros_str.append(str(numero))

# print(', '.join(list(set(numeros))))