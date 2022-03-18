import requests
from src.utils import *

# Get base URL
def _url(path):
    return POKEAPI_URL + path            

# Get all pokemon object 
def get_pokemons(limit: int = None):
    resp = requests.get(_url('/pokemon/'), params = {'limit': limit}) 
    pokemon_list = []
    if resp.status_code == 200:
        payload = resp.json()
        pokemon_list = payload.get('results', [])
    return pokemon_list

# Get egg groups name from pokemon
def get_egg_groups_name(pokemon):
    resp = requests.get(_url('/pokemon-species/' + pokemon))
    egg_groups_names = []
    if resp.status_code == 200:
        payload = resp.json()
        egg_groups = payload.get('egg_groups', [])
        if egg_groups:
            for egg_group in egg_groups:
                egg_groups_names.append(egg_group['name'])
    return egg_groups_names         

# Get pokemon names from egg group
def get_pokemon_name_from_egg_group(egg_group):
    resp = requests.get(_url('/egg-group/' + egg_group))
    pokemon_names = []
    if resp.status_code == 200:
        payload = resp.json()
        pokemon_list = payload.get('pokemon_species', [])
        if pokemon_list:
            for pokemon in pokemon_list:
                pokemon_names.append(pokemon['name'])
    return pokemon_names

# Get pokemon list by type and generation
def get_pokemon_by_type(type, generation = 'first'):
    range_generation = {
        'first': {'start': START, 'end': END}
    }
    resp = requests.get(_url('/type/' + type))
    pokemon_name = []
    if resp.status_code == 200:
        payload = resp.json()
        pokemon_list = payload.get('pokemon', [])
        if pokemon_list:
            for pokemon in pokemon_list:
                id = pokemon['pokemon']['url'].split('/')[6]
                if (int(id) <= range_generation[generation]['end']):
                    pokemon_name.append(pokemon['pokemon']['name'])
    return pokemon_name

# Get pokemon weight by name
def get_pokemon_weight(name): 
    resp = requests.get(_url('/pokemon/' + name))
    if resp.status_code == 200:
        payload = resp.json()
        weight = payload.get('weight', [])
        return weight
