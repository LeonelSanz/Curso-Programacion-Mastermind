from random import randint
from os import system

print("La mazmorra del Destino\n"
      "--------------------\n"
      "\n"
      "En lo más profundo del Reino Olvidado yacía la temida Mazmorra del Destino.\n"
      "Se decía que aquel valiente que lograra llegar a su núcleo obtendría un poder inigualable.\n"
      "Aventureros de todas partes se lanzaban a la oscuridad en busca de renombre y gloria.\n"
      "\n"
      "Tú, un intrépido guerrero, decides adentrarte en las entrañas de la mazmorra.\n"
      "Las paredes húmedas gotean con un líquido desconocido, y el aire está impregnado de una tensión palpable.\n"
      "Después de explorar pasillos y enfrentarte a criaturas tenebrosas, llegas a una bifurcación.\n"
      "A tu izquierda, un pasaje angosto con una tenue luz al final. "
      "A tu derecha, una puerta pesada con inscripciones misteriosas. ¿Qué camino elegirás?"
      )

opcion = input("Opcion [A] - Derecha | Opcion [B] - Izquierda ")
system("cls")

if opcion == "A":
    print("Abres la puerta pesada, revelando una habitación llena de espejos mágicos que reflejan versiones "
          "futuras de ti mismo.\nCada reflejo te ofrece un consejo diferente sobre cómo superar la mazmorra.")
    opcion = input("Opcion [A] - Sigues el consejo de la astucia | Opcion [B] - Decides tocar un espejo ")
    system("cls")

    if opcion == "A":
        print("Utilizas el conocimiento adquirido para sortear trampas y evitar encuentros peligrosos.\n"
              "Llegas a una sala con dos salidas: una puerta con una cerradura complicada y un túnel estrecho.\n"
              "¿Qué camino tomarás?")
        opcion = input("Opcion [A] - Puerta con cerradura | Opcion [B] - Tunel ")


        if opcion == "A":
            print("Logras abrir la cerradura y encuentras un atajo que te lleva directo al núcleo de la mazmorra.")
        elif opcion == "B":
            print("Te deslizas por el túnel y descubres una cámara secreta llena de tesoros.")


    elif opcion == "B":
        num_random = randint(1, 100)
        print("Intrigado por los espejos, decides tocar uno de ellos.\n"
              "De repente, te ves envuelto en una energía oscura que consume tu ser.\n"
              "Una criatura guardiana emerge de las sombras y te pregunta cuanto es 18 * {}".format(num_random))

        opcion = int(input("Cual es el resultado? "))

        if opcion == 18 * num_random:
            print("La criatura te dice que te salvaste pero que nunca vuelvas a la mazmorra.")
        else:
            print("La criatura guardiana emergida de las sombras, sin piedad, te aniquila.\n"
                  "Tu aventura llega a su fin en la oscura mazmorra.")


elif opcion == "B":
    print("Te aventuras por el estrecho pasillo, y gradualmente la luz aumenta.\n"
          "Descubres una cámara resplandeciente donde una figura encapuchada te ofrece una elección:\n"
          "una espada que promete fuerza inigualable o un amuleto que concede astucia y velocidad.\n"
          "¿Qué tomarás?")
    opcion = input("Opcion [A] - Espada | Opcion [B] - Amuleto ")
    system("cls")

    amuleto = False

    if opcion == "A":
        print("Agarras la espada")
    elif opcion == "B":
        amuleto = True
        print("Agarras el amuleto")
    else:
        print("No aceptas el regalo de la figura encapuchada, se enoja y te mata.")
        exit()

    print("Ahora, enfrentas la segunda decisión: continuar hacia adelante o retroceder y explorar el pasaje no tomado.")
    opcion = input("Opcion [A] - Avanzar | Opcion [B] - Retroceder ")

    if opcion == "A" and amuleto:
        print("Encuentras un enfrentamiento con un guardián mágico.\n"
              "El guardian es muy poderoso y buscas la forma de escapar\n"
              "Como tienes el amuleto puedes escapar facilmente.")
    elif opcion == "B":
        print("Al regresar al pasillo, encuentras un atajo secreto que te lleva más profundo en la mazmorra, "
              "evitando encuentros peligrosos.")
    else:
        print("Encuentras un enfrentamiento con un guardián mágico.\n"
              "El guardian es muy poderoso y te mata.")

else:
    print("No has elegido ninguna opcion. Simplemente mueres.")