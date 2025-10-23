# Faça um programa em que o usuário deverá digitar
# os nomes de dez alunos da sala de aula. Em seguida,
# caso o programa encontre nomes repetidos, ele deverá
# alterar o nome adicionando o número sequencial. Por
# exemplo, se na lista tivermos dois "José", após o
# processamento a lista deverá conter "José 1" e "José 2".

nomes = []
contagem = {}
for i in range(3):
    nome = input('Digite o nome de um aluno: ')
    

    if nome in contagem:
        contagem[nome] += 1
        nomes_final = f"{nome} {contagem[nome]}"
    else:
        contagem[nome] = 1
        nomes_final = f"{nome} {contagem[nome]}"
            
    nomes.append(nomes_final)
for n in nomes:
    print(n)

