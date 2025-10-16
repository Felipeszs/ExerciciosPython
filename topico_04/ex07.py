# Usando tupla, resolva:
# Crie um programa que receba uma
# data como string no formato dd/mm/aaaa.
# Em seguida, retorne a data por extenso.
# Por exemplo, dada a entrada "14/10/2025",
# retorne "14 de outubro de 2025".

meses_por_extenso = (
    'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
    'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
)
data_user = input('Digite uma data (dd/mm/aaaa): ')

partes_data = data_user.split('/')

numero_do_mes = int(partes_data[1])

nome_do_mes = meses_por_extenso[numero_do_mes - 1]

print(f'{partes_data[0]} de {nome_do_mes} de {partes_data[2]}')