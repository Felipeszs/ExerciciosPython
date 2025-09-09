# Crie um programa para uma empresa de energia que cobra tarifas
# progressivas com base no consumo mensal em kWh, de acordo com a
# seguinte tabela:
#  Até 50 kWh: R$ 0,30 por kWh
#  De 51 a 150 kWh: R$ 0,40 por kWh
#  De 151 a 300 kWh: R$ 0,50 por kWh
#  Acima de 300 kWh: R$ 0,70 por kWh
# O programa deverá receber a quantidade de kWh e mostrar o valor total
# a ser pago pelo cliente.

consumo_mensal = int(input('Digite o consumo mensal: '))

if consumo_mensal < 50:
    print(consumo_mensal * 0.30)
elif consumo_mensal < 150:
    print(consumo_mensal * 0.40)
elif consumo_mensal < 300:
    print(consumo_mensal * 0.50)
else:
    print(consumo_mensal * 0.70)