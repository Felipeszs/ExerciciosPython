# Faça um programa que contenha duas listas com 5 posições.
# Na primeira lista, deverá ser inserido o nome dos alunos.
# Na segunda lista, na mesma posição, a nota do aluno. Em
# seguida, mostre o nome dos alunos com a maior e a menor nota.
nomes = []
notas = []

for i in range(5):
    nomes.append(input('Digite o nome do aluno: '))
    notas.append(float(input('Digite a nota do aluno: ')))

nome_maior_nota = nomes[notas.index(max(notas))]
nome_menor_nota = nomes[notas.index(min(notas))]

print(nome_maior_nota, nome_menor_nota)

