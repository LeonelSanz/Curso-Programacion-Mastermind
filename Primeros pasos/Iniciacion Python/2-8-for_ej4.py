
"""
lista_nums = []
num = int(input("Introduzca un numero en la lista "))
lista_nums.append(num)

while input("Desea introducir otro numero? [S/N] ") == "S"
    num = int(input("Introduzca un numero en la lista "))
    lista_nums.append(num)
"""

numeros_introducidos = input("Introduzca los numeros separados por coma: ")
numeros_de_usuario = [int(numero) for numero in numeros_introducidos.split(",")]

# print("numero mas pequenio: {}".format(min(numeros_de_usuario)))
# print("numero mas grande: {}".format(max(numeros_de_usuario)))

numero_pequenio = numeros_de_usuario[0]
numero_grande = numeros_de_usuario[0]

for numero in numeros_de_usuario[1:]:
    if numero_pequenio > numero:
        numero_pequenio = numero

    if numero_grande < numero:
        numero_grande = numero

print("Numero grande: {}, numero pequenio: {}".format(numero_grande, numero_pequenio))