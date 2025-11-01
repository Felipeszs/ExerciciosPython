# Pangrama, ou pantograma, (do grego, pan ou
# pantós = todos, + grama = letra) é uma frase 
# em que são usadas todas as letras do alfabeto 
# de determinada língua. A partir da definição, 
# crie um código python para definir se uma frase 
# é ou não um pangrama.
# https://pt.wikipedia.org/wiki/Pangrama

import string


# Use como exemplo a frase:
frase = 'Jane quer LP, fax, CD, giz, TV e bom whisky'

alfabeto = set()

frase = set(frase.lower())

print(frase >= alfabeto)
