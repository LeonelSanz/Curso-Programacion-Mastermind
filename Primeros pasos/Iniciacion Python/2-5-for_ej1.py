
frase = input("Escribe una frase ")
espacios = 0
puntos = 0
comas = 0

for a in frase:
    if a == " ":
        espacios += 1
    elif a == ".":
        puntos += 1
    elif a == ",":
        comas += 1

print("Espacios: {}".format(espacios))
print("Puntos: {}".format(puntos))
print("Comas: {}".format(comas))
