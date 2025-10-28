# Implemente em Python um jogo de cartas 21 (Black Jack simplificado),
# utilizando as estruturas de dados dict e list. O jogo
# deve permitir que o jogador dispute contra o computador, somando
# valores de cartas até chegar o mais próximo possível de 21 pontos,
# sem ultrapassar esse valor. Cada carta deve ser representada como
# um dicionário contendo o número e o naipe, e o baralho deve ser
# uma lista embaralhada de cartas. O jogador e o computador devem
# receber duas cartas iniciais, e novas cartas podem ser retiradas
# do sempre do final do baralho. O programa deve exibir as cartas
# e pontuações finais, indicando o vencedor. Utilize o código abaixo
# como base para a definição dos naipes:

import random

# Set up the constants:
HEARTS = chr(9829)    # Character 9829 is '♥'
DIAMONDS = chr(9830)  # Character 9830 is '♦'
SPADES = chr(9824)    # Character 9824 is '♠'
CLUBS = chr(9827)     # Character 9827 is '♣'

naipes = [HEARTS, DIAMONDS, SPADES, CLUBS]
baralho = []

for i in range(1,11):
    for naipe in naipes:
        baralho.append({'numero': i, 'naipe': naipe})

random.shuffle(baralho)

jogador = {'cartas': [], 'pontuacao': 0}
computador = {'cartas': [], 'pontuacao': 0}

jogador['cartas'].append(baralho.pop())
jogador['cartas'].append(baralho.pop())

computador['cartas'].append(baralho.pop())
computador['cartas'].append(baralho.pop())

while True:
    print(jogador['cartas'])

    if input('Deseja mais carta? ') != 's':
        break

    jogador['cartas'].append(baralho.pop())
    jogador['pontuacao'] = sum([carta['numero'] for carta in jogador['cartas']])

    if jogador['pontuacao'] > 21:
        break

computador['pontuacao'] = sum([carta['numero'] for carta in computador['cartas']])

while computador['pontuacao'] < 17:
    computador['cartas'].append(baralho.pop())
    computador['pontuacao'] = sum([carta['numero'] for carta in computador['cartas']])

print(computador['cartas'])

if jogador['pontuacao'] > 21:
    print('Você perdeu!')
elif computador['pontuacao'] > 21:
    print('Você ganhou!')
elif jogador['pontuacao'] > computador['pontuacao']:
    print('Você ganhou')
else:
    print('Você perdeu!')
