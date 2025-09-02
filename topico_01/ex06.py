# Crie um programa que leia dois números e uma
# operação (soma, subtração, multiplicação ou divisão)
# do usuário. Realize a operação correspondente
# e mostre o resultado.

numero1 = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))
operador = input('digite o operador [+, -, *, /]')
exp = f'{numero1} {operador} {numero2}'
resultado = eval(exp) # evitar usar.
print(resultado)
