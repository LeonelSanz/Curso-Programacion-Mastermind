import string

frase = input("Introduce una frase ")

mayusculas = 0

for a in frase:
    if a in string.ascii_uppercase:
        mayusculas += 1

print("Mayusculas: {}".format(mayusculas))