# Exercise 5.3: Get the height and weight of a specific Pokemon and print the output
#
# Extension: Print the names of all of a specific Pokemon's moves

import requests #include this but make sure you run 'pip install requests' first
from pprint import pprint

pokemonId = input('which pokemon information do you want?')
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemonId) # step 1 get url string

response = requests.get(url) #step 2 sending the request

pokemon = response.json()  # step 3 converting to a readable format
print(pokemon['name'])
print(pokemon['height'])
print(pokemon['weight'])
for move in pokemon['moves']:
    pprint(move['move']['name'])