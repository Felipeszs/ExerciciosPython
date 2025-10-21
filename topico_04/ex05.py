# Faça um programa em que o usuário deverá digitar
# os nomes de dez alunos da sala de aula. Em seguida,
# caso o programa encontre nomes repetidos, ele deverá
# alterar o nome adicionando o número sequencial. Por
# exemplo, se na lista tivermos dois "José", após o
# processamento a lista deverá conter "José 1" e "José 2".

# nomes = ['Maria', 'Pedro', 'Maria', 'João', 'Pedro']
nomes = []
for i in range(10):
    nomes.append(input('Digite o nome: '))

for nome in nomes:

    if nomes.count(nome) == 1:
        continue

    count = 1
    for index, _nome in enumerate(nomes):
        if nome == _nome:
            nomes[index] = f'{nome} {count}'
            count += 1

print(nomes)