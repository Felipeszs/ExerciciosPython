#Itens em Comum (Interseção Simples) Dadas duas listas de compras, 
# mostre quais itens aparecem em ambas as listas.

compras_1 = ["maçã", "banana", "leite", "pão"]

compras_2 = ["banana", "ovos", "leite", "café"]

print(set(compras_1).intersection(set(compras_2)))