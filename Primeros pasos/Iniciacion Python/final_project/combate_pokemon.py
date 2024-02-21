import random
from pprint import pprint
from pokeload import get_all_pokemons

"""
PROYECTO FINAL

En estas últimas cinco clases hemos comenzado el increíble proyecto Batalla Pokémon. Como último paso antes de terminar este apasionante camino aprendiendo a programar con Python queremos que lo finalices y nos muestres los resultados que has obtenido.

1.- Utiliza el desarrollo que se realiza en las primeras clases capturando los datos de los 150 Pokémon básicos. Para ello sigue los pasos de las clases Pokemon Survival, Capturando los 150 y Recordando pepinillos y crea el fichero pokeload.py.

2.- A partir del desarrollo de clase de Pokemons random y Comienza el combate se inicia el fichero combate_pokemon.py completa el reto con:

  2.1 .- Desarrolla los métodos necesarios para que se realice el ataque y defensa tanto del jugador como del enemigo, teniendo en cuenta tanto la vida actual de cada Pokémon, su experiencia, nivel y tipo de Pokémon.

  2.2 .- Desarrolla las funciones y código necesario para que el jugador pueda realizar "acciones" tal y como se introducen (Capturar con PokéBall, Lanzar curación u otras).

  2.3 .- Desarrolla una interfaz fluida a través de consola que permita:

         - Visualizar el estado del combate con la vida de cada uno de los Pokémon.

         - Visualizar el inventario de Pokémon.

         - Visualizar el inventario de pociones.

         - Visualizar los combates realizados.

  2.4 .- Modificar y ampliar la función de puntos de batalla y la subida de experiencia.

  2.5 .- Como extra implementar la evolución Pokémon.



¡LET´S GO!
"""

def get_player_profile(pokemon_list):
    return {
        "player_name": input("Cual es tu nombre? "),
        "pokemon_inventory": [random.choice(pokemon_list) for a in range(3)],
        "combats": 0,
        "pokeballs": 0,
        "health_potion": 0,
    }


def any_player_pokemon_lives(player_profile):
    return sum([pokemon["current_health"] for pokemon in player_profile["pokemon_inventory"]]) > 0


def choose_pokemon(player_profile):
    chosen = None
    while not chosen:
        print("Elige con que pokemon lucharas")
        for index in range(len(player_profile["pokemon_inventory"])):
            print("{} - {}".format(index, get_pokemon_info(player_profile["pokemon_inventory"][index])))
        try:
            return player_profile["pokemon_inventory"][int(input("Cual eliges? "))]
        except (ValueError, IndexError):
            print("Opcion invalida")


def get_pokemon_info(pokemon):
    return "{} | lvl {} | hp {}/{}".format(pokemon['name'],
                                           pokemon["level"],
                                           pokemon["current_health"],
                                           pokemon["base_health"])


def player_attack(player_pokemon, enemy_pokemon):
    """ Implementar multiplicadores de dmg en base al tipo de pokemon
        *1.25

        cuando se elige el ataque del usuario, solo se muestran los ataques disponibles en ese nivel
    """
    pass


def enemy_attack(enemy_pokemon, player_pokemon):
    pass


def assign_experience(attack_history):
    for pokemon in attack_history:
        points = random.randint(1, 5)
        pokemon["current_exp"] += points

    while pokemon["current_exp"] > 20:
        pokemon["current_exp"] -= 20
        pokemon["level"] += 1
        pokemon["current_health"] = pokemon["base_health"]
        print("Tu pokemon ha subido al nivel {}".format(get_pokemon_info(pokemon["level"])))


def cure_pokemon(player_profile, player_pokemon):
    pass


def capture_with_pokeball(player_profile, enemy_pokemon):
    pass


def fight(player_profile, enemy_pokemon):
    print("--- NUEVO COMBATE ---")

    attack_history = []
    player_pokemon = choose_pokemon(player_profile)
    print("Contrincantes: {} VS {}".format(get_pokemon_info(player_pokemon),
                                           get_pokemon_info(enemy_pokemon)))

    while any_player_pokemon_lives(player_profile) and enemy_pokemon["current_health"] > 0:
        action = None
        while action not in ["A", "P", "V", "C"]:
            action = input("Que deseas hacer? [A]tacar, [P]okeball, Pocion de [V]ida, [C]ambiar")

        if action == "A":
            player_attack(player_pokemon, enemy_pokemon)
            attack_history.append(player_pokemon)
        elif action == "P":
            # Hay una probabilidad de capturar relativa a la salud restante, cuando se captura pasa al inventario
            capture_with_pokeball(player_profile, enemy_pokemon)
        elif action == "V":
            # Si el usuario tiene curas, se aplica, cura 50 de vida hasta llegar a 100
            # si usuario no tiene no se cura
            cure_pokemon(player_profile, player_pokemon)
        elif action == "C":
            player_pokemon = choose_pokemon(player_profile)

        enemy_attack(enemy_pokemon, player_pokemon)

        if player_pokemon["current_health"] == 0 and any_player_pokemon_lives(player_profile):
            player_pokemon = choose_pokemon(player_profile)

    if enemy_pokemon["current_health"] == 0:
        print("Has ganado!")
        assign_experience(attack_history)

    print("--- FIN DEL COMBATE ---")
    input("Presiona ENTER para continuar")


def item_lottery(player_profile):
    """ Segun un factor aleatorio, al jugador le puede tocar una pokeball o una cura"""


def main():
    pokemon_list = get_all_pokemons()
    player_profile = get_player_profile(pokemon_list)

    while any_player_pokemon_lives(player_profile):
        enemy_pokemon = random.choice(pokemon_list)
        fight(player_profile, enemy_pokemon)
        item_lottery(player_profile)

    print("Has perdido en el combate n{}".format(player_profile["combats"]))


if __name__ == "__main__":
    main()
