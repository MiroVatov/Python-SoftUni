
class Trainer:

    def __init__(self, name: str):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon) -> str:
        if pokemon not in self.pokemon:
            self.pokemon.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        else:
            return f"This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str) -> str:
        pokemons = [p for p in self.pokemon if p.name == pokemon_name]
        if pokemons:
            self.pokemon.remove(pokemons[0])
            return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        data = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon)}\n- "
        for p in self.pokemon:
            data += p.pokemon_details() + "\n"
        return data

