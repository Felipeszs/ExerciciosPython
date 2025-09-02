# Implemente um programa que tenha como entrada o valor em
# reais e mostre o valor correspondente em dólar.
import requests

URL = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'

response = requests.get(URL)
COTACAO = response.json()
COTACAO = float(COTACAO.get('USDBRL').get('bid'))

reais = float(input('Digite o valor em reais: '))

dolares = round(reais / COTACAO, 2)

print(f'{reais} corresponde a {dolares} dolares.')
