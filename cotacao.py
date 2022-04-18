import requests
import json

cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
cotacoes = cotacoes.json()
cotacao_dollar = cotacoes['USDBRL']['bid']
#print(cotacoes)
print(cotacao_dollar)