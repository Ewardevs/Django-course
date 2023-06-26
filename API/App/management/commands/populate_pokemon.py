import requests
from django.core.management.base import BaseCommand
from App.models import Pokemon

class Command(BaseCommand):
    help = 'Populates the Pokemon model with data from the Poke API.'

    def handle(self, *args, **options):
        response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=1281hghgh')
        data = response.json()

        for result in data['results']:
            pokemon_url = result['url']
            pokemon_response = requests.get(pokemon_url)
            pokemon_data = pokemon_response.json()

            name = pokemon_data['name']
            types = [t['type']['name'] for t in pokemon_data['types']]
            attack = pokemon_data['stats'][1]['base_stat']
            defense = pokemon_data['stats'][2]['base_stat']
            image_url = pokemon_data['sprites']['front_default']

            pokemon = Pokemon(
                name=name,
                type=', '.join(types),
                attack=attack,
                defense=defense,
                image_url=image_url
            )
            pokemon.save()