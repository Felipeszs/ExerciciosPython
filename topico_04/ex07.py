# Usando tupla, resolva:
# Crie um programa que receba uma
# data como string no formato dd/mm/aaaa.
# Em seguida, retorne a data por extenso.
# Por exemplo, dada a entrada "14/10/2025",
# retorne "14 de outubro de 2025".

meses = ('jan.', 'fev.', 'mar.', 'abr', 'maio', 'jun','jul', 'ago')

data = input('Digite a data de nascimento: ')

dia, mes, ano = data.split('/')

print(f'{dia} de {meses[int(mes) - 1]} de {ano}')