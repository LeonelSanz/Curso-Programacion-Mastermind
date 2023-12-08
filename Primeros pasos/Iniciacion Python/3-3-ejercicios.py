from random import randint

# Ejercicio 1: La string más larga
# Crea una funcion que reciba una lista de strings como entrada y te diga cual es la más larga de todas
# Ejemplo:
# string_mas_larga("hola", "como", "estas")
# > "estas"

def string_mas_larga(string, *args):
    string_larga = string
    for a in args:
        if len(a) > len(string_larga):
            string_larga = a
    return string_larga


# Ejercicio 2: Sumando la lista
# Crea una función que sume una lista de números, no se vale usar la función sum()
# Ejemplo:
# suma([1, 2, 3, 4, 5])
# > 15

def suma(nums):
    resultado = 0
    for a in nums:
        resultado += a
    return resultado


# Ejercicio 3: Par o impar
# Crea una función que te de True como resultado si el número pasado como argumento es impar
# Ejemplo:
# es_impar(3)
# > True
# es_impar(24)
# > False

def es_impar(num):
    if num % 2 == 0:
        return False
    return True


# Ejercicio 4: Pregunta algo
# Crea una función que pregunte al usuario si esta seguro o no,
# y devuelva los valores "True" o "False" dependiendo de si el usuario está seguro.

def esta_seguro():
    seguro = input("Estas seguro? [S/N] ")
    if seguro == "S":
        return True
    return False

# Ejercicio 5: A mayus
# Crea una función que convierta toda una string en mayusculas, no vale usar el método upper()

def mayus(string):
    resultado = ""
    for char in string:
        if 'a' <= char <= 'z':
            mayuscula = chr(ord(char) - ord('a') + ord('A'))
            resultado += mayuscula
        else:
            resultado += char
    return resultado

# Ejercicio 6: Adivina el número
# Crea una función que reciba como argumento un número del 1 al 100 a adivinar y que le pregunte
# al usuario que adivine el número. El código se ejecutará hasta que el usuario adivine.

def adivina_el_numero():
    num_random = randint(1, 10)
    num_usuario = 0
    while num_usuario != num_random:
        num_usuario = int(input("Adivina el numero "))
    return "Muy bien, acertaste, el numero era {}".format(num_usuario)

# Ejercicio 7: Lista de la compra
# Crea una función que dada una lista de la compra definida fuera de la función,
# permita al usuario añadir un nuevo item asegurandose que no exista anteriormente en la lista.

def add_to_list(list):
    add = input("Añade un nuevo item ")
    for a in list:
        if add != a:
            list.append(add)
            print("{} añadido a la lista".format(add))
        else:
            print("{} ya esta en la lista".format(add))
        return


def main():
    # print(string_mas_larga("hola", "como", "estas", "a", "123456"))
    # print(suma([1, 2, 3, 4, 5, 15]))
    # print(es_impar(33))
    # print(esta_seguro())
    # print(mayus("Hola, como estas?"))
    # print(adivina_el_numero())
    lista_compra = ["Leche", "Harina"]
    add_to_list(lista_compra)


if __name__ == "__main__":
    main()
