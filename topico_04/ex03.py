# Faça um programa que crie uma lista vazia. Em seguida,
# o usuário deverá informar as notas de trabalhos obtidas
# (pode variar de 0 até quantos trabalhos forem informados).
# Por fim, mostre a média aritmética das notas obtidas.
notas = []

while True:
    nota = float(input('Digite uma nota: '))
    notas.append(nota)

    continuar = input('Deseja informar outra nota [S/N]?')
    if continuar.lower() == 'n':
        break

media = sum(notas) / len(notas)
# print(round(media, 2))
print(f'{media:.2f}')