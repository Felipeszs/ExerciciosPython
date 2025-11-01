#O Elemento Intruso (Diferença Simétrica) Você tem duas listas de números que deveriam ser idênticas, 
# mas um "número intruso" foi adicionado em uma delas. 
# Encontre esse número. (É uma variação do seu primeiro exemplo).

lista_A = [5, 10, 15, 20, 25]
lista_B = [10, 25, 5, 99, 15, 20]

if len(lista_A) > len(lista_B):
    print(set(lista_A) - set(lista_B))
else: print(set(lista_B) - set(lista_A))