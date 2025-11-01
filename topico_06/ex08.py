# Elementos Exclusivos (Diferença Simples) Dadas duas listas de convidados, 
# mostre quais convidados estão na primeira lista, 
# mas não estão na segunda.

convidados_A = ["Ana", "Bruno", "Carla", "Daniel"]

convidados_B = ["Bruno", "Daniel", "Eva", "Fábio"]

print(set(convidados_A).difference(set(convidados_B)))