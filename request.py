import requests


def fetch_pokemon(name):
    response = requests.get(
        f"https://pokeapi.co/api/v2/pokemon/{name}").json()
    return response['sprites']['front_default']


def fetch_dogs():
    response = requests.get(
        'https://dog.ceo/api/breeds/image/random').json()
    return response['message']


def fetch_cep(cep):
    response = requests.get(
        f"https://brasilapi.com.br/api/cep/v1/{cep}").json()
    return f"Cidade: {response['city']} Estado: {response['state']} Cep: {response['cep']}"


def fetch_kanye():
    response = requests.get('https://api.kanye.rest/').json()
    return response['quote']
