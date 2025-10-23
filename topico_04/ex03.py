# Faça um programa que crie uma lista vazia. Em seguida,
# o usuário deverá informar as notas de trabalhos obtidas
# (pode variar de 0 até quantos trabalhos forem informados).
# Por fim, mostre a média aritmética das notas obtidas.
notas = []
<<<<<<< HEAD
i = 0
notas_soma = 0
while True:
    nota = int(input('Digite a nota: '))
    notas.append(nota)
    notas_soma += notas[i]
    i += 1
    continuar_laco = input('Deseja continuar adicionando notas (S para continuar)')
    if continuar_laco != 'S':
        break
print(len(notas))
print(notas_soma)
media = notas_soma / len(notas)
print(media)



notas2 = []

while True:

    nota_trabalho = float(input('Digite a nota do trabalho: '))

    notas2.append(nota_trabalho)

    continuar = input('Deseja adicionar outra nota? (S para continuar): ').upper()

    if continuar != 'S':
        break

soma_das_notas = sum(notas2)

quantidade_de_notas = len(notas2)

media = soma_das_notas / quantidade_de_notas

# Exibe os resultados
print("\n--- Resultados ---")
print(f"Notas informadas: {notas2}")
print(f"Soma das notas: {soma_das_notas}")
print(f"Média das notas: {media:.2f}")
=======

while True:
    nota = float(input('Digite uma nota: '))
    notas.append(nota)

    continuar = input('Deseja informar outra nota [S/N]?')
    if continuar.lower() == 'n':
        break

media = sum(notas) / len(notas)
# print(round(media, 2))
print(f'{media:.2f}')
>>>>>>> 1c50802b07658cedb5ccde52674efa6de41d4c78
