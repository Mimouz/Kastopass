import requests

res = requests.get('https://www.castorama.pl/cataloginventory/index/checkAvailabilityInStores?show_all_markets=true&qty=1&sku=318070')

print(res.text)
#print(res.status_code)