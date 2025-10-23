# Dadas duas lista que são duplicadas uma da
# outra, exceto por um elemento, ou seja, um 
# elemento de uma das listas está faltando. 
# Mostre-o usando conjuntos.
lista1 = [4, 8, 15, 16, 23, 42]
lista2 = [4, 8, 15, 23, 42]  

print(set(lista1) - set(lista2))