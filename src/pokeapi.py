import requests
from typing import Union
from src.utils import *

# Get Base URL in UTILS and add PATH
def _url(path):
    return POKEAPI_BASE_URL + path            

# Get JSON all pokemons data 
def get_pokemons(limit: int = None):
    response = requests.get(_url('/pokemon/'), params = {'limit': limit}) 
    pokemon_list = []
    if response.status_code == 200:
        payload = response.json()
        pokemon_list = payload.get('results', [])
    return pokemon_list

# Get JSON egg groups name from pokemon data
def get_egg_groups_name(pokemon: Union[str, int]):
    response = requests.get(_url('/pokemon-species/' + pokemon))
    egg_groups_names = []
    if response.status_code == 200:
        payload = response.json()
        egg_groups = payload.get('egg_groups', [])
        if egg_groups:
            for egg_group in egg_groups:
                egg_groups_names.append(egg_group['name'])
    return egg_groups_names         

# Get JSON pokemon names from egg group data
def get_pokemon_name_from_egg_group(egg_group: Union[str, int]):
    response = requests.get(_url('/egg-group/' + egg_group))
    pokemon_names = []
    if response.status_code == 200:
        payload = response.json()
        pokemon_list = payload.get('pokemon_species', [])
        if pokemon_list:
            for pokemon in pokemon_list:
                pokemon_names.append(pokemon['name'])
    return pokemon_names

# Get JSON pokemon list by type and generation data
def get_pokemon_by_type(type, generation = 'first'):
    range_generation = {
        'first': {'start': START, 'end': END}
    }
    response = requests.get(_url('/type/' + type))
    pokemon_name = []
    if response.status_code == 200:
        payload = response.json()
        pokemon_list = payload.get('pokemon', [])
        if pokemon_list:
            for pokemon in pokemon_list:
                id = pokemon['pokemon']['url'].split('/')[6]
                if (int(id) <= range_generation[generation]['end']):
                    pokemon_name.append(pokemon['pokemon']['name'])
    return pokemon_name

# Get JSON pokemon weight by name data
def get_pokemon_weight(name: Union[str, int]): 
    response = requests.get(_url('/pokemon/' + name))
    if response.status_code == 200:
        payload = response.json()
        weight = payload.get('weight', [])
        return weight
