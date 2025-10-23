# Dadas três listas de números inteiros,
# imprima os elementos comuns entre elas.
a = [1, 3, 5, 7, 9]
b = [2, 3, 6, 7, 10]
c = [0, 3, 4, 7, 11]
for n in a:
    if n in b and n in c:
        print(n)
