# Você recebe uma string e sua tarefa é trocar casos. 
# Em outras palavras, converta todas as letras minúsculas
# em maiúsculas e vice-versa.
# Input: Fatec Rio Preto
# Output: fATEC rIO pRETO

frase = input('Digite uma frase: ')

for letra in frase:
    if letra.islower() == True:
        print(letra.upper(), end='')
    else:
        print(letra.lower(), end='')