# Faça um programa que contenha duas listas com 5 posições.
# Na primeira lista, deverá ser inserido o nome dos alunos.
# Na segunda lista, na mesma posição, a nota do aluno. Em
# seguida, mostre o nome dos alunos com a maior e a menor nota.

nome_alunos = []
nota_alunos = []
maior_nota = 0
menor_nota = 0
for i in range (3):
    nome_alunos.append(input('Digite o nome do aluno: '))
    nota_alunos.append(int(input(f'Digite a nota de {nome_alunos[i]}: ')))
    if i == 0:
        maior_nota = nota_alunos[i]
        menor_nota = nota_alunos[i]
    elif nota_alunos[i] > maior_nota:
        maior_nota = nota_alunos[i]
    elif nota_alunos[i] < menor_nota:
        menor_nota = nota_alunos[i]

print('\nAluno(s) com a maior nota:')
for i in range(3):
    if nota_alunos[i] == maior_nota:
        print(f'{nome_alunos[i]} - {nota_alunos[i]}')

print('\nAluno(s) com a menor nota:')
for i in range(3):
    if nota_alunos[i] == menor_nota:
        print(f'{nome_alunos[i]} - {nota_alunos[i]}')

