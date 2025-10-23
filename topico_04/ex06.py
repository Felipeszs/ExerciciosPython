# Implemente o jogo da forca. Um usuário deverá entrar 
# com uma palavra. Em seguida, outro usuário deverá 
# indicar as letras dessa palavra. Caso exista, deverá 
# ser mostrada as letras e as suas posições na palavra. 
# Caso não exista, o usuário perderá uma chance. No total, 
# o usuário terá 6 chances para acertar.


palavra_certa = input('Digite uma palavra para o jogo da forca: ').lower()
progresso = ['_'] * len(palavra_certa)
quantidade_erros = 0
quantidade_chances = 6

while quantidade_erros < quantidade_chances:
    print(f'Você tem {quantidade_chances - quantidade_erros} chances para acertar a palavra ')
    print('palavra', ' '.join(progresso))
    letra_tentativa = input('Digite uma letra: ').lower()
    if letra_tentativa in palavra_certa:
        for i in range(len(palavra_certa)):
            if palavra_certa[i] == letra_tentativa:
                progresso[i] = letra_tentativa
        print(f"A letra '{letra_tentativa}' está na palavra!")
    else:
        print(f"A letra {letra_tentativa} não está na palavra")
        quantidade_erros += 1
    
    if '_' not in progresso:
        print("\n🎉 Parabéns! Você acertou a palavra:", palavra_certa)
        break
else:
    print("\n😢 Suas chances acabaram. A palavra era:", palavra_certa)
    
##OU TBM PODE SER 
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

