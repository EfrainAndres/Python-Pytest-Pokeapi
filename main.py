from src.pokeapi import *
from src.utils import *

# First question
def first_question():
    result = []
    pokemon_list = get_pokemons(SIZE_POKEMON_LIST)
    for pokemon in pokemon_list:
        name = pokemon['name']
        if 'at' in name and name.count('a') == 2:
            result.append(name)
    return len(result)                

# Second question         
def second_question():
    egg_groups_names = get_egg_groups_name('raichu')
    pokemon_names = []
    for egg_group_name in egg_groups_names:   
        pokemon_names_egg_group = get_pokemon_name_from_egg_group(egg_group_name)
        pokemon_names.extend(pokemon_names_egg_group)
    return len(list(dict.fromkeys(pokemon_names)))    

# Third question
def third_question():
    pokemon_list = get_pokemon_by_type('fighting')  
    widths = []
    for pokemon in pokemon_list:
        widths.append(get_pokemon_weight(pokemon))
    return [max(widths), min(widths)]    

def check_answers_solutions():
    questions = (
        first_question,
        second_question,
        third_question,
    )

    for question in questions:
        n = questions.index(question) + 1
        if n == 1:
            print("\n¿Cuantos pokemones poseen en sus nombres \"at\" y tienen 2 \"a\" en su nombre, incluyendo la primera del \"at\"?")
            print(first_question())
        if n == 2:
            print("\n¿Con cuántas especies de pokémon puede procrear raichu? (2 Pokémon pueden procrear si están dentro del mismo egg group).")
            print(second_question())
        if n == 3:
            print("\nEntrega el máximo y mínimo peso de los pokémon de tipo fighting de primera generación (cuyo id sea menor o igual a 151).")
            print(third_question())

check_answers_solutions()