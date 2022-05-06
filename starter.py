# How do I output the species values for each of the dictionaries?

animals = [
    {'species': 'zebra', 'name': 'Penelope'},
    {'species': 'penguin', 'name': 'Jenn'},
    {'species': 'elephant', 'name': 'Harris'},
    {'species': 'flamingo', 'name': 'Florence'},
]

for animal in animals:
    name = animal['name']
    species = animal['species']
    print('{} is a {}.'.format(name, species))