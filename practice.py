import requests

api_key = '50f60326-728e-45c3-8455-bce8e50e4fcf'
word = 'voluminous'
root_url = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json'
final_url = f'{root_url}/{word}?key={api_key}'
r = requests.get(final_url)
result = r.json()
print(result)