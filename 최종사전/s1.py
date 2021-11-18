import requests
from pprint import pprint

my_key = 'f9c334c81c11d7992f72a49191ff61b4'
url = f'https://api.themoviedb.org/3/search/multi?api_key={my_key}&language=en-US&query=lalaland&page=1&include_adult=false'
url1 = f'https://api.themoviedb.org/3/configuration/countries?api_key={my_key}'
response = requests.get(url)
response1 = requests.get(url1)
res = response.text
res1 = response1.json()
# print(type(res))
# pprint(res)
pprint(res)
# pprint(res1)
# print(url)