# DESAFIO: Crie um cógifo em python que teste se o site Pudim está acessível pelo computador usado.
import requests
try:
    url = requests.get("http://pudim.com.br/")
except:
    print("O servidor está indisponível.")
else:
    print('Tudo ok')
