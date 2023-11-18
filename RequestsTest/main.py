import requests
from tokens import trainer_token

host = 'https://api.pokemonbattle.me:9104'

response = requests.post(url=f'{host}/pokemons',
                        json={
                             "name": "Pokemon",
                             "photo": "https://dolnikov.ru/pokemons/albums/021.png"},
                        headers={'Content-Type':'application/json',
                                'trainer_token': trainer_token},
                        timeout=5)
print(f'Message:{response.text}')

response = requests.put(url=f'{host}/pokemons',
                        json={
                             "pokemon_id": "19821",
                             "name": "Pokemon_3",
                             "photo": "https://dolnikov.ru/pokemons/albums/121.png"},
                        headers={'Content-Type':'application/json',
                                'trainer_token': trainer_token},
                        timeout=5)
print(f'Message:{response.text}')

response = requests.post(url=f'{host}/trainers/add_pokeball',
                        json={"pokemon_id": "19821"},
                        headers={'Content-Type':'application/json',
                                'trainer_token': trainer_token},
                        timeout=5)
print(f'Message:{response.text}')