# Dadas duas lista que são duplicadas uma da
# outra, exceto por um elemento, ou seja, um 
# elemento de uma das listas está faltando. 
# Mostre-o usando conjuntos.

x = [1, 2, 3, 4]
y = [1, 2, 4]

print(set(x) - set(y))

k = set(x) | set(y) # {1, 2, 3, 4}
v = set(x) & set(y) # {1, 2, 4}

k - v # {3}

set(x) ^ set(y)
