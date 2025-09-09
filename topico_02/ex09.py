# Escreva um programa que receba três valores numéricos representando
# os lados de um triângulo e determine se os valores podem formar um
# triângulo válido (a soma de dois lados deve ser sempre maior que o
# terceiro). Se for válido, classifique-o como: Equilátero: todos os 
# lados iguais; Isósceles: dois lados iguais; ou Escaleno: todos os 
# lados diferentes.

a = int(input('Digite a: '))
b = int(input('Digite b: '))
c = int(input('Digite c: '))

if a + b > c and c + b > a and a + c > b:
    if a == b and b == c:
        print('Triângulo Equilátero')
    elif a != b and b != c and a != c:
        print('Triângulo Escaleno')
    else:
        print('Triângulo Isósceles')
else:
    print('Não é um triângulo.')