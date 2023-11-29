from os import system
from random import randint

VIDA_INICIAL_PIKACHU = 80
VIDA_INICIAL_SQUIRTLE = 90

vida_pikachu = VIDA_INICIAL_PIKACHU
vida_squirtle = VIDA_INICIAL_SQUIRTLE

TAMANIO_BARRA_VIDA = 20

while VIDA_INICIAL_PIKACHU > 0 and VIDA_INICIAL_SQUIRTLE > 0:
    # Se desenvuelven los turnos de combate

    print("Turno de Pikachu")
    ataque_pikachu = randint(1, 2)

    if ataque_pikachu == 1:
        # Bola Voltio
        print("Pikachu ataca con Bola Voltio")
        vida_squirtle -= 10
    else:
        print("Pikachu ataca con Onda Trueno")
        vida_squirtle -= 11

    if vida_squirtle < 0:
        vida_squirtle = 0

    if vida_pikachu < 0:
        vida_pikachu = 0
    
    barra_pikachu = int(vida_pikachu * TAMANIO_BARRA_VIDA / VIDA_INICIAL_PIKACHU)
    print("Pikachu:\t[{}{}] ({}/{})".format("*" * barra_pikachu, " " * (TAMANIO_BARRA_VIDA - barra_pikachu),
                                            vida_pikachu, VIDA_INICIAL_PIKACHU))

    barra_squirtle = int(vida_squirtle * TAMANIO_BARRA_VIDA / VIDA_INICIAL_SQUIRTLE)
    print("Squirtle:\t[{}{}] ({}/{})".format("*" * barra_squirtle, " " * (TAMANIO_BARRA_VIDA - barra_squirtle),
                                             vida_squirtle, VIDA_INICIAL_SQUIRTLE))

    input("Enter para continuar...\n\n")
    system("cls")

    print("Turno Squirtle")

    ataque_squirtle = None
    while ataque_squirtle not in ["P", "A", "B", "N"]:
        ataque_squirtle = input("Que ataque deseas realizar? [P]lacaje, Pistola [A]gua, [B]urbuja, [N]ada: ")

    if ataque_squirtle == "P":
        print("Squirtle ataca con Placaje")
        vida_pikachu -= 10
    elif ataque_squirtle == "A":
        print("Squirtle ataca con Pistola Agua")
        vida_pikachu -= 12
    elif ataque_squirtle == "B":
        print("Squirtle ataca con Burbuja")
        vida_pikachu -= 9
    elif ataque_squirtle == "N":
        print("Squirtle no hace nada...")

    if vida_squirtle < 0:
        vida_squirtle = 0

    if vida_pikachu < 0:
        vida_pikachu = 0

    barra_pikachu = int(vida_pikachu * TAMANIO_BARRA_VIDA / VIDA_INICIAL_PIKACHU)
    print("Pikachu:\t[{}{}] ({}/{})".format("*" * barra_pikachu, " " * (TAMANIO_BARRA_VIDA - barra_pikachu),
                                            vida_pikachu, VIDA_INICIAL_PIKACHU))

    barra_squirtle = int(vida_squirtle * TAMANIO_BARRA_VIDA / VIDA_INICIAL_SQUIRTLE)
    print("Squirtle:\t[{}{}] ({}/{})".format("*" * barra_squirtle, " " * (TAMANIO_BARRA_VIDA - barra_squirtle),
                                             vida_squirtle, VIDA_INICIAL_SQUIRTLE))

    input("Enter para continuar...\n\n")
    system("cls")

if vida_pikachu > vida_squirtle:
    print("Pikachu gana")
else:
    print("Squirtle gana")