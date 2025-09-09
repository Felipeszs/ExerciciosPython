# Faça um programa para jogar Jokenpô (clássico pedra, papel 
# e tesoura) com você. Você deverá informar uma das opções, 
# o programa deverá então sortear uma das três opções possíveis
# e mostrar quem ganhou na tela.

import random

# computador = random(0, 2)

# if computador == 0:
#     computador = 'pedra'
# elif computador == 1:
#     computador = 'papel'
# else: 
#     computador = 'tesoura'

computador = random.choice(['pedra', 'papel', 'tesoura'])

usuario = input('Digite uma opção: ')
usuario = usuario.lower()

if computador == usuario:
    print('Empate')
elif (computador == 'pedra' and usuario == 'tesoura' or 
      computador == 'papel' and usuario == 'pedra' or
      computador == 'tesoura' and usuario == 'papel'):
    print('Computador ganhou.')
else:
    print('Usuário ganhou.')
