# Faça um programa que crie dois conjuntos x e y,
# com dez números inteiros cada um. Em seguida, crie:
# 1) Um conjunto resultante da união de x e y (todos os
# elementos de x e os elementos de y que não estão em x).
# 2) Um conjunto resultante da diferença entre x e y (todos
# os elementos de x que não existam em y).
# 3) Um conjunto resultante interseção entre x e y
x = {1, 4, 53, 22, 45, 10}
y = {3, 5, 45, 27, 84, 36}
uniao = x.union(y)
diferença = x.difference(y)
intersecao = x.intersection(y)
print(f'Uniao de x e y: {uniao} \nDiferenca de x e y: {diferença} \nIntersecao de x e y: {intersecao} ')