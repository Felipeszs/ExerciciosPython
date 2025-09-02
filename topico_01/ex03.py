# Supondo que queremos pintar o muro da instituição, faça um programa
# que leia a altura e a largura do muro e mostre a quantidade de tinta
# necessária (1 litro de tinta pode pintar uma área de 2 metros quadrados).

altura = int(input('Digite a altura: '))
largura = int(input('Digite a largura: '))

area = altura * largura

quantidade_tinta = area / 2

print(f'Você utilizará {quantidade_tinta} litros de tinta.')
