# Implemente em Python um jogo de cartas 21 (Blackjack simplificado),

# utilizando as estruturas de dados dict e list. O jogo

# deve permitir que o jogador dispute contra o computador, somando valores

# de cartas até chegar o mais próximo possível de 21 pontos, sem ultrapassar

# esse valor. Cada carta deve ser representada como um dicionário contendo

# o número e o naipe, e o baralho deve ser uma lista embaralhada de cartas.

# O jogador e o computador devem receber duas cartas iniciais, e novas cartas

# podem ser retiradas do sempre do final do baralho. O programa deve

# exibir as cartas e pontuações finais, indicando o vencedor. Utilize o

# código abaixo como base para a definição dos naipes:



# Set up the constants:

import random

# --- Constantes (como no seu código) ---
HEARTS = chr(9829)    # Character 9829 is '♥'
DIAMONDS = chr(9830)  # Character 9830 is '♦'
SPADES = chr(9824)    # Character 9824 is '♠'
CLUBS = chr(9827)     # Character 9827 is '♣'

naipes = [HEARTS, DIAMONDS, SPADES, CLUBS]
numeros = [1, 2 , 3, 4, 5, 6, 7, 8, 9, 10]

baralho = []
for naipe in naipes:
    for numero in numeros:
        carta = {'numero': numero, 'naipe': naipe}
        baralho.append(carta)

random.shuffle(baralho)

mao_jogador = []
mao_pc = []

mao_jogador.append(baralho.pop())
mao_pc.append(baralho.pop())
mao_jogador.append(baralho.pop())
mao_pc.append(baralho.pop())

pontos_jogador = 0
pontos_pc = 0

print("--- Jogo de 21 (Blackjack Simplificado) ---")

while (True):

    pontos_jogador = sum(carta['numero'] for carta in mao_jogador)
    
    print(f'\nVocê tem {pontos_jogador} pontos')

    print(f'Sua mão: {mao_jogador}')  

    if pontos_jogador > 21:
        print('Você estourou (passou de 21)!')
        break
    elif pontos_jogador == 21:
        print('Você fez 21!')
        break


    x = input('Você deseja pegar uma carta? (s/n): ').lower()

    if x == 'n':
        break 
    elif x == 's':

        nova_carta = baralho.pop()
        mao_jogador.append(nova_carta)
        print(f'Você pegou: {nova_carta}')
    else:
        print("Opção inválida. Digite 's' ou 'n'.")

pontos_jogador = sum(carta['numero'] for carta in mao_jogador)


pontos_pc = sum(carta['numero'] for carta in mao_pc)

if pontos_jogador <= 21:
    print('\n--- Vez do Computador ---')
    print(f'Mão inicial do PC: {mao_pc} ({pontos_pc} pontos)')
    

    while pontos_pc < 17:
        print('O computador pega uma carta...')
        nova_carta_pc = baralho.pop()
        mao_pc.append(nova_carta_pc)
        
        pontos_pc = sum(carta['numero'] for carta in mao_pc)
        print(f'Nova mão do PC: {mao_pc} ({pontos_pc} pontos)')

    if pontos_pc > 21:
        print('O computador estourou!')
    else:
        print(f'O computador parou com {pontos_pc} pontos.')


print('\n--- Resultado Final ---')
print(f'Sua mão: {mao_jogador}')
print(f'A mao do jogador é {pontos_jogador}')

print(f'Mão do PC: {mao_pc}')
print(f'A mao do pc é {pontos_pc}')

if pontos_jogador > 21:
    print('Você perdeu (estourou)!')
elif pontos_pc > 21:
    print('Você ganhou (computador estourou)!')
elif pontos_jogador > pontos_pc:
    print('Você ganhou!')
elif pontos_pc > pontos_jogador:
    print('Você perdeu (computador tem mais pontos)!')
else:
    print('Empate!')