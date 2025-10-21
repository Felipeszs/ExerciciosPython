# Implemente o jogo da forca. Um usuário deverá entrar 
# com uma palavra. Em seguida, outro usuário deverá 
# indicar as letras dessa palavra. Caso exista, deverá 
# ser mostrada as letras e as suas posições na palavra. 
# Caso não exista, o usuário perderá uma chance. No total, 
# o usuário terá 6 chances para acertar.

palavra = input('Digite uma palavra: ')

user = ['_'] * len(palavra)

chances = 6

while chances > 0:

    print(''.join(user))

    letra = input('Digite uma letra: ')

    if letra not in palavra:
        chances -= 1
        continue

    for index, _letra in enumerate(palavra):
        if letra == _letra:
            user[index] = _letra

    if user.count('_') == 0:
        print('Você venceu!')
        break

else:
    print('Você perdeu!')