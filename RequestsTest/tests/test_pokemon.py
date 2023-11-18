import requests
import pytest

host = 'https://api.pokemonbattle.me:9104'

def test_status_code():
    response = requests.get(url=f'{host}/trainers', timeout=5)
    assert response.status_code==200

def test_trainer_name():
    response = requests.get(url=f'{host}/trainers', 
                            params={'trainer_id':'2559'},
                            timeout=5 )
    assert response.json()['trainer_name']=='Elena'