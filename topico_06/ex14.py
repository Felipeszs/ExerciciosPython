#O Elemento Faltante (Seu primeiro problema) 
# Este é o seu primeiro exercício, que é um excelente exemplo de uso da diferença simétrica.
# Encontre o elemento faltante (4) usando uma única operação de conjunto.

lista_original = [1, 5, 2, 8, 4, 9, 3]

lista_modificada = [9, 2, 5, 1, 8, 3]

print(set(lista_original) ^ set(lista_modificada))